#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 09_ADC_ldr_leds.py
# Leitura analógica de um fotoresistor (LDR), com exibição numa escala de leds.
#
from machine import Pin, ADC
from time import sleep

ldr = ADC(0)
leds = [
    Pin(12, Pin.OUT),
    Pin(13, Pin.OUT),
    Pin(15, Pin.OUT)
    ]

def mapear_escala(valor, min, max, faixas):
    valor_p = (valor - min) / (max - min)
    print('valor:', valor, '(', 100*valor_p, '%)', end=' ')
    for n_led in range(len(leds)):
        estado = valor_p > (n_led + 1) / faixas
        leds[n_led].value(estado)
        print(n_led, ':', estado, '|', end=' ')
    print()
    
try:
    while True:
        valor = ldr.read()
        mapear_escala(valor, 0, 1023, 4)
        sleep(2.0)
except KeyboardInterrupt:
    print('Programa finalizado')
