#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 11_i2c_scan.py
# Scanner de dispositivos conectados compatíveis com protocolo I2C.
#
from machine import Pin, I2C
from os import uname

i2c_bus = I2C(sda=Pin(5), scl=Pin(4))

print('Pesquisando dispositivos I2C conectados ao', uname()[0],'...')
dispositivos = i2c_bus.scan()

num_disp = len(dispositivos)
if num_disp:
    print(num_disp, 'endereço(s) reconhecido(s): \n| ', end='')
    for dispositivo in dispositivos: print(hex(dispositivo), end=' |')
    print()
else:
    print('Nenhum dispositivo encontrado')
