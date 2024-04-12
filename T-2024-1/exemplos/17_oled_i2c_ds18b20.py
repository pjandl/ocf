#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 17_oled_i2c_ds18b20.py
# Coleta de múltiplas temperaturas por meio de sensores
# DS18B20, conectados com barramento OneWire, e exibição dos
# dados em display OLED I2C.
#
from machine import Pin, I2C
from time import sleep, sleep_ms
import onewire
import ds18x20
import ssd1306

# Configura barramento I2C
i2c = I2C(sda=Pin(4), scl=Pin(5))
# Cria objeto p/ controle do display OLED 128x64 I2C
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

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
        sleep(10)
except KeyboardInterrupt:
    oled.poweroff()