#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 04_botao_led_buzzer.py
# Um botão para acionamento do led externo.
#
from machine import Pin
from time import sleep

# saída conectada ao led externo
led = Pin(15, Pin.OUT)
# saída conectada ao buzzer
buzzer = Pin(12, Pin.OUT)
# entrada conectada à chave táctil
botao = Pin(14, Pin.IN)

try:
    while True:
        if botao.value():
            led.value(1)
            for n in range(6):
                buzzer.value(n % 2 == 0)
                sleep(0.05)
            sleep(0.1)
            led.value(0)
        sleep(0.1)
except KeyboardInterrupt:
    led.value(0)
    buzzer.value(0)
    print('Programa finalizado')
