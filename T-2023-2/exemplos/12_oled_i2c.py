#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 12_oled_i2c.py
# Uso de display OLED conectado com protocolo I2C.
#
from machine import Pin, I2C
from time import sleep
import ssd1306

# Configura barramento I2C
i2c = I2C(sda=Pin(4), scl=Pin(5))
# Cria objeto p/ controle do display OLED 128x64 I2C
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

pen = 1 # 1 ativa pontos, 0 desliga pontos
for r in range(4):
    oled.fill(not pen) # preenche display
    oled.rect(0, 0, 128, 16, pen) # retangulo
    oled.text('Ola!', 2, 4, pen) # escreve texto em x,y
    oled.show() # renderiza desenhos e texto
    sleep(3.0)
    oled.text('Tudo bem?', 2, 18, pen)
    oled.show()
    sleep(3.0)
    oled.text('01234567890+-*/', 2, 54, pen)
    oled.text('abcdefghijklmno', 2, 30, pen)
    oled.text('pqstuvxz     =)', 2, 42, pen)
    oled.show()
    sleep(5.0)
    pen = not pen # inverte caneta
    
oled.poweroff() # desliga display
