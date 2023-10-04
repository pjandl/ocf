#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 16_ts_oled_bmp180_i2c.py
# Coleta de temperatura, pressão e altitude por sensor BMP180 I2C,
# com exibição dos dados em display OLED I2C e envio para dashboard
# na plataforma de IoT ThingSpeak.
#
from bmp180 import BMP180
from machine import Pin, I2C
from utime import sleep, gmtime
import network
import ssd1306
import urequests

# ThingSpeak Write API KEY
TS_WRITE_KEY = 'ZQHVVUYTVOLLT3GF'
# URL para conexão com ThingSpeak service
url = "https://api.thingspeak.com/update?api_key={}&field1={}&field2={}&field3={}"

# Configura barramento I2C
i2c = I2C(sda=Pin(4), scl=Pin(5))

# Cria objeto p/ controle do display OLED 128x64 I2C
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
# Configuração OLED pontos: 1 = ligados; 0 = desligados
PEN = 1 

# Cria e ajusta objeto p/ controle do sensor BMP180
bmp180 = BMP180(i2c)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

# Função para conexão com a WiFi
def conectaWiFi():
    # Estabelece modo de funcionamento estação (STA_IF)
    estacao = network.WLAN(network.STA_IF)
    # Ativa transceiver Wi-Fi
    estacao.active(True)
    # Conecta da rede ssid com senha
    estacao.connect(WIFI_SSID, WIFI_PASS)
    t = 60
    while not estacao.isconnected()\
          and estacao.status() >= 0\
          and t > 0:
        print('.', end='')
        t -= 1
        sleep(1.0)
    if not estacao.isconnected():
        raise RuntimeError('Falha na conexão de rede')
    print('\nConexão Wifi OK:\n', estacao.ifconfig())
    return estacao


# SSID Wifi
WIFI_SSID = 'j4nd1'
WIFI_PASS = 'abc1abc2abc3'
# Estabele conexão com rede WiFi/Internet
estacao = conectaWiFi()

try:
    f = ' '
    while True:
        oled.fill(not PEN) # preenche display
        oled.rect(0, 0, 128, 16, PEN) # desenha retangulo
        
        t = bmp180.temperature
        p = bmp180.pressure/100
        a = bmp180.altitude
        
        if not estacao.isconnected():
            estacao = conectaWiFi()
            
        if estacao.isconnected():
            # envia HTTP get ao ThingSpeak com valor aleatório
            resposta = urequests.get(url.format(TS_WRITE_KEY, t, p, a))
            # verifica se resposta OK (código 200)
            if resposta.status_code == 200:
                # obtém e exibe texto da resposta
                texto = resposta.text
                # verifica se ocorreu gravação dos dados
                f = '+' if int(texto) != 0 else '-'
                print('Resposta:', texto, f)

        oled.text('{} Estacao TPA {}'.format(f, f),   2,  4, PEN)
        oled.text('Temp : ' + str(round(t,1)) + '*C', 2, 24, PEN)
        oled.text('Press: ' + str(round(p,1)) + 'mB', 2, 38, PEN)
        oled.text('Alt  : ' + str(round(a,1)) + 'm' , 2, 52, PEN)
        oled.show()
        
        sleep(120.0)

except KeyboardInterrupt:
    oled.poweroff() # desliga display
    estacao.active(False) # desliga transceiver WiFi
    print('Programa finalizado')
    