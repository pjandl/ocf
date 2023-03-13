#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 03_dois_leds_externos.py
# Acionamento dos leds externos à placa.
#
from machine import Pin
from time import sleep

led1 = Pin(15, Pin.OUT)
led2 = Pin(13, Pin.OUT)

while True:
    led1.value(1)
    sleep(0.5)
    led1.value(0)
    sleep(0.5)
    led2.value(1)
    sleep(0.5)
    led2.value(0)
    sleep(0.5)
