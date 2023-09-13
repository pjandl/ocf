#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 06_botao_led_rele.py
# Um botão, com manutenção de estado, para controle
# de um relê, com led externo de sinalização.
#
from machine import Pin
from time import sleep

# saída conectada ao led externo
led = Pin(15, Pin.OUT)
# entrada conectada à chave táctil
botao = Pin(12, Pin.IN)

estado = False
led.value(estado)
print('Controle:', estado)
ultimo = estado
try:
    while True:
        valor = botao.value()
        if valor and not ultimo:
            estado = not estado
            led.value(estado)
            print('Controle:', estado)
        ultimo = valor
        sleep(0.2)
except KeyboardInterrupt:
    led.value(0)
    print('Programa finalizado')
