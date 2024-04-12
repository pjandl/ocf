#
# Oficina de Computa莽茫o F铆sica
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
s = ' '
while True:
    oled.fill(not pen) # preenche display
    oled.rect(0, 0, 128, 16, pen) # retangulo
    
    t = bmp180.temperature
    p = bmp180.pressure/100
    a = bmp180.altitude
    
    oled.text('{} Estacao TPA {}'.format(s, s), 2, 4, pen)
    oled.text('Temp : ' + str(round(t,1)) + '*C', 2, 24, pen)
    oled.text('Press: ' + str(round(p,1)) + 'mB', 2, 38, pen)
    oled.text('Alt  : ' + str(round(a,1)) + 'm', 2, 52, pen)
    oled.show()
    
    s = '*' if s == ' ' else '*'
    sleep(15.0)
    
oled.poweroff() # desliga display
