#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 11_i2c_bh1750.py
# Uso de protocolo I2C para obtenção de dados de sensor de luminosidade BH1750.
#
from machine import Pin, I2C
from bh1750 import BH1750
from time import sleep
    
i2c_bus = I2C(sda=Pin(5), scl=Pin(4))

# Sensor BH1750
bh = BH1750(i2c=i2c_bus)

try:
    while True:
#         print('Luminosidade :', sample(i2c_bus))
        print('Luminosidade :', bh.luminance)
        sleep(3.0)
except KeyboardInterrupt:
    print('Programa finalizado')
