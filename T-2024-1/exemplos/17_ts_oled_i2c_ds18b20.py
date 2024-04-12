#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 17_oled_i2c_ds18b20.py
# Coleta de múltiplas temperaturas por meio de sensores
# DS18B20, conectados com barramento OneWire, e exibição dos
# dados em display OLED I2C e envio para dashboard na
# plataforma de IoT ThingSpeak.
#
from machine import Pin, I2C
from time import sleep, sleep_ms
import onewire
import ds18x20
import network
import ssd1306
import urequests

# Configura barramento I2C
i2c = I2C(sda=Pin(4), scl=Pin(5))
# Cria objeto p/ controle do display OLED 128x64 I2C
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# ThingSpeak Write API KEY
TS_WRITE_KEY = 'YMG8KQ009WM5XCP5'
# URL para conexão com ThingSpeak service
url = "https://api.thingspeak.com/update?api_key={}&field1={}&field2={}&field3={}&field4={}&field5={}&field6={}&field7={}&field8={}"

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
WIFI_SSID = 'FamJandl-ext1'
WIFI_PASS = 'pj15mcp19hp20'

# Estabele conexão com rede WiFi/Internet
estacao = conectaWiFi()

# Configura barramento OneWire
ds_net = ds18x20.DS18X20(onewire.OneWire(Pin(2)))
# Obtém lista de endereços de dispositivos OneWire
ds_list = ds_net.scan()
print('Dispositivos DS encontrados:\n[ ', end='')
for addr in ds_list:
    print(addr.hex(), ', ', sep='', end='') 
print(']')

try:
    temp = []
    for n in range(len(ds_list)): temp.append(0)
    msg = '{}:{} = {:.2f}*C'
    while True:
        print(28*'=')
        oled.fill(0) # limpa display
        # Solicita captura de temperatura
        ds_net.convert_temp()
        # Leitura só pode ocorre após 750ms
        sleep_ms(750)
        avg = 0
        for n in range(len(ds_list)):
            temp[n] = ds_net.read_temp(ds_list[n])
            avg += temp[n]
            print(msg.format(n, ds_list[n].hex(), temp[n]))
        avg /= len(ds_list)       
        oled.text(msg.format(1, 'min', min(temp)), 1,  0, 1)
        oled.text(msg.format(2, 'avg', avg),       1, 12, 1)
        oled.text(msg.format(3, 'max', max(temp)), 1, 24, 1)
        oled.show()
        # Verifica conexão com WiFi        
        if not estacao.isconnected():
            estacao = conectaWiFi()
        # Envia dados            
        if estacao.isconnected():
            # envia HTTP get ao ThingSpeak com valores das temperaturas
            resposta = urequests.get(url.format(TS_WRITE_KEY, temp[0], temp[1],\
                                                temp[2], temp[3], temp[4],\
                                                temp[5], temp[6], avg))
            # verifica se resposta OK (código 200)
            if resposta.status_code == 200:
                # obtém e exibe texto da resposta
                texto = resposta.text
                # verifica se ocorreu gravação dos dados
                f = '+' if int(texto) != 0 else '-'
                print('Resposta:', texto, f)
        sleep(60)
except KeyboardInterrupt:
    oled.poweroff()