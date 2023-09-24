# OFC::13 Display OLED e Sensor Barométrico I2C 

Esta montagem toma como base a anterior [OFC::12 Display OLED I2C](https://github.com/pjandl/ocf/blob/main/T-2023-2/12_oled_i2c.md), na qual um display OLED 128x64 é conectado ao NodeMCU ESP8266 por meio do barramento **I2C** para exibição de informações. Aqui será acrescentado um sensor barométrico BMP180 I2C, compartilhando o barramento existente, mostrando quão flexível e conveniente é este protocolo para interligação de múltiplos dispositivos. 

O sensor barométrico BMP180 é um módulo de dimensões reduzidas, capaz de capturar a pressão atmosférica e a temperatura ambiente, com precisão suficiente para que possa ser utilizado como altímetro. A interface elétrica deste componente é I2C, permitindo que seja facilmente conectado a outros dispositivos para troca de informações.

Assim, com uso de apenas duas GPIO para o barramento I2C, conectaremos o ESP8266 à um display OLED e ao módulo sensor BMP180.

## Objetivo

Uso do barramento I2C para conexão simultânea com múltiplos dispositivos por meio de entradas digitais. A informação coletada pelo sensor BMP180 será apresentada no display OLED da montagem.

## Lista de Materiais

* Placa NodeMCU ESP8266 (30 pinos)
* Cabo USB-A -- USB-C
* 01 Display OLED 128x64 I2C
* 01 Módulo sensor BMP180
* 01 Protoboard (170 pontos ou mais)
* Jumpers

## Roteiro

Este roteiro requer a montagem simples indicada na figura que segue, onde o barramento de quatro linhas/vias I2C é conectado ao display e ao módulo sensor:
+ **SDA** : *serial data line*, por onde trafegam os dados entre os dispositivos conectados;
+ **SCL** : *serial clock line*, que controla as operações de comunicação;
+ **GND** : *ground*, comum da alimentação; e
+ **VCC** : tensão de alimentação.

![Circuito 13 OLED BMP180 I2C](https://github.com/pjandl/ocf/blob/main/T-2023-2/figuras/13_oled_bmp180_i2c.png)

Observe as conexões entre o NodeMCU, o protoboard, o display e o módulo sensor para constituir o barramento I2C: linha 4 para SDA, linha 5 para SCL, linha 6 para GND e linha 7 para VCC. 

*Preste atenção nas conexões com o display e o módulo sensor, pois a pinagem **não** é padronizada e varia conforme o fabricante!*

Com esta montagem e o código que segue, é possível exibir informações coletadas pelo módulo sensor BMP180 no display OLED conectados ao NodeMCU pelo barramento I2C.

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
# 13_oled_bmp180_i2c.py
# Uso de display OLED e sensor BMP180 conectados com protocolo I2C.
#
from bmp180 import BMP180
from machine import Pin, I2C
from time import sleep
import ssd1306

# Configura barramento I2C
i2c = I2C(sda=Pin(4), scl=Pin(5))
# Cria objeto p/ controle do display OLED 128x64 I2C
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Cria e ajusta objeto p/ controle do sensor BMP180
bmp180 = BMP180(i2c)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

pen = 1 # 1 ativa pontos, 0 desliga pontos
while True:
    oled.fill(not pen) # preenche display
    oled.rect(0, 0, 128, 16, pen) # retangulo
    
    t = bmp180.temperature
    p = bmp180.pressure/100
    a = bmp180.altitude
    
    oled.text('Estacao TPA', 2, 4, pen)
    oled.text('Temp : ' + str(round(t,1)) + '*C', 2, 24, pen)
    oled.text('Press: ' + str(round(p,1)) + 'mB', 2, 38, pen)
    oled.text('Alt  : ' + str(round(a,1)) + 'm', 2, 52, pen)
    oled.show()
    
    sleep(5.0)
    
oled.poweroff() # desliga display

```

6. Salve como "13_oled_bmp180_i2c.py".
7. Para executar acione o botão *Executar* ou **F5**.
8. Devem ser exibidas no display OLED as informações de temperatura, pressão e altitude coletadas pelo sensor BMP180, as quais são atualizadas a cada 5 segundos.
9. Observe que com uso da variável `pen = 1`, as mensagens são escritas com pontos ativos e fundo inativo (apagado), enquanto com `pen = 0`, as mensagens são escritas com pontos inativos e fundo ativo (ativado).

---

Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2023-2
