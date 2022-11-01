#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 11_i2c_bmp280.py
# Uso de protocolo I2C para obtenção de dados de sensor barométrico BMP280.
#
from machine import Pin, I2C
from bmp280 import BME280
from time import sleep
    
i2c_bus = I2C(sda=Pin(4), scl=Pin(5))

# Sensor BMP280
bme = BME280(i2c=i2c_bus)

try:
    while True:
        print('Temperatura :', bme.temperature)
        sleep(1.0)
        print('    Pressão :', bme.pressure)
        sleep(1.0)
        print('    Umidade :', bme.humidity)
        sleep(3.0)
except KeyboardInterrupt:
    print('Programa finalizado')
