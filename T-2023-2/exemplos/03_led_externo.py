#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 03_led_externo.py
# Acionamento do led externo à placa.
#
from machine import Pin
from time import sleep

led1 = Pin(15, Pin.OUT)

while True:
    led1.value(1)
    sleep(0.5)
    led1.value(0)
    sleep(0.5)
