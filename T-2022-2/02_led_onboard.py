#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 02_led_onboard.py
# Acionamento do led existente na placa.
#
from machine import Pin
from time import sleep

led_onboard = Pin(16, Pin.OUT)

while True:
 led_onboard.value(1)
 sleep(0.5)
 led_onboard.value(0)
 sleep(2)
 