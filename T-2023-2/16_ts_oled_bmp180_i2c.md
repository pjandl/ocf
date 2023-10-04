# OFC::16 ThingSpeak, Display OLED e Sensor Barométrico

Nesta montagem vamos combinar as capacidades do NodeMCU ESP8266 de se conectar a redes **Wi-Fi** (*Wireless Fidelity*) para enviar dados ao serviço da internet **ThingSpeak** e de coletar dados por meio de um sensor barométrico BMP180.

Utilizaremos como ponto de partida a montagem realizada na experiência [13_oled_bmp180_i2c.md](../13_oled_bmp180_i2c.md), na qual conectamos um sensor barométrico BMP180, capaz de coletar a temperatura, pressão atmosférica e altitude local; e um display OLED 128x64; ao NodeMCU ESP8266 por meio de uma barramento **I2C** (*Inter-Integrated Circuit*).

Esta montagem e seu *script* serão combinados com a experiência [15_thingspeak.md](../15_thingspeak.md), de maneira que a placa, o sensor e o display passam a constituir uma pequena estação de coleta de dados metereológicos, que serão exibidos no display e enviados a um canal do ThingSpeak (https://thingspeak.com), plataforma de IoT (Internet das Coisas) que permite a configuração de um *dashboard* no qual serão exibidos e disponibilizados os dados coletados publicamente.

## Objetivo

Construir uma miniestação metereológica, capaz de coletar dados de temperatura, pressão atmosférica e altitude, enviando-os para um *dashboard* na plataforma **ThingSpeak**.

## Lista de Materiais

* Placa NodeMCU ESP8266 (30 pinos)
* Cabo USB-A -- USB-C
* 01 Display OLED 128x64 I2C
* 01 Módulo sensor BMP180
* 01 Protoboard (170 pontos ou mais)
* Jumpers

## Roteiro

Este roteiro requer a montagem simples indicada na figura que segue, onde o barramento de quatro linhas/vias I2C é conectado ao display e ao módulo sensor:

![Circuito 13 OLED BMP180 I2C](https://github.com/pjandl/ocf/blob/main/T-2023-2/figuras/13_oled_bmp180_i2c.png)

Observe as conexões entre o NodeMCU, o protoboard, o display e o módulo sensor para constituir o barramento I2C: linha 4 para SDA, linha 5 para SCL, linha 6 para GND e linha 7 para VCC. 

> :warning: **Aviso:** Preste atenção nas conexões com o display, pois a pinagem *não* é padronizada e varia conforme o fabricante!

Com esta montagem e o código que segue, é possível exibir informações coletadas pelo módulo sensor BMP180 no display OLED conectados ao NodeMCU pelo barramento I2C, além do envio destes dados para a plataforma ThingSpeak.

1. Efetue a montagem indicada. Confira todas as conexões.
2. Conecte a placa NodeMCU à porta USB de seu computador.
3. Abra o Thonny.
4. Observe se o console do interpretador Python é iniciado corretamente. Caso contrário: verifique em *Executar | Configurar interpretador* se o interpretador foi selecionado corretamente (MicroPython ESP8266) e se a porta de conexão está correta. Acione o botão *Stop* ou **CTRL+F2** para reiniciar a conexão.
5. Digite o sketch que segue.

```python
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
    

```

6. Salve como "16_ts_oled_bmp180_i2c.py".
7. Para executar acione o botão *Executar* ou **F5**.
8. Os dados coletados devem ser exibidos no display OLED. No console do Thonny são impressas mensagem indicativas do recebimento adequado dos dados enviados ao ThingSpeak: um inteiro acompanhado de `+` indica sucesso da gravação e o número do registro; o sinal `-` indica um erro. O programa efetua o envio dos dados com um intervalo de 2 minutos para cada envio. Modifique se julgar necessário.

![Thonny Consooe](https://github.com/pjandl/ocf/blob/main/T-2023-2/figuras/16_console.png)

9. Carregue a url https://thingspeak.com/channels/2291348 no seu navegador para visualizar o dashboard do canal, observando o recebimento de novos dados a cada 2 minutos.

![ThingSpeak Channel](https://github.com/pjandl/ocf/blob/main/T-2023-2/figuras/16_ts_channel.png)

> :warning: **Aviso:** Para que seja possível o registro de dados, é necessário o envio da *chave da API*, um código numérico que funciona como uma autorização para a gravação de dados. Cada canal possui uma chave própria, que pode ser obtida na configuração do canal na plataforma ThingSpeak. No início deste script, definimos a variável `TS_WRITE_KEY` para conter a chave do canal utilizado.

---

Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2023-2
