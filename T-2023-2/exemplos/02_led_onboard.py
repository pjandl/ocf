#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 02_led_onboard.py
# Acionamento do led existente na placa.
#
# O led onboard do ESP8266 é ativado em baixo, com value(0)
# ou off(), e desligado com value(1) ou on().
#
from machine import Pin
from time import sleep

# led integrado na placa
led_onboard = Pin(2, Pin.OUT)

while True:
    led_onboard.value(0)
    sleep(0.5)
    led_onboard.value(1)
    sleep(2.0) 
