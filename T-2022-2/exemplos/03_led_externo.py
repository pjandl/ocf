#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 03_led_externo.py
# Acionamento do led externo à placa.
#
from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT)

while True:
 led.value(1)
 sleep(0.5)
 led.value(0)
 sleep(2.0)
 