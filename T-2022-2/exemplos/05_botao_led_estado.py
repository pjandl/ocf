#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 05_botao_led_estado.py
# Um botão, com manutenção de estado, para acionamento do
# led externo.
#
from machine import Pin
from time import sleep

# saída conectada ao led externo
led = Pin(15, Pin.OUT)
# entrada conectada à chave táctil
botao = Pin(14, Pin.IN)

estado = 0
ultimo = 0
try:
    while True:
        valor = botao.value()
        if valor == 1 and ultimo == 0:
            estado = not estado
            led.value(estado)
        ultimo = valor
        sleep(0.2)
except KeyboardInterrupt:
    led.value(0)
    print('Programa finalizado')
