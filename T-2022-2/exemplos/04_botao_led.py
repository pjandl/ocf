#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 04_botao_led.py
# Um botão para acionamento do led externo.
#
from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT)
botao = Pin(14, Pin.IN)

try:
    while True:
        led.value(botao.value())
        sleep(0.1)
except KeyboardInterrupt:
    led.value(0)
    print('Programa finalizado')
