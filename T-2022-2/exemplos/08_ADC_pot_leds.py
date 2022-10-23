#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 08_ADC_pot_leds.py
# Leitura analógica de um potenciômetro, com exibição numa escala de leds.
#
from machine import Pin, ADC
from time import sleep

pot = ADC(0)
ledAzul = Pin(12, Pin.OUT)
ledBran = Pin(13, Pin.OUT)
ledVerm = Pin(15, Pin.OUT)

def escala(azul, branco, vermelho):
            ledAzul.value(azul)
            ledBran.value(branco)
            ledVerm.value(vermelho)
    
try:
    while True:
        valor = pot.read()
        valor_p = 100 * (valor / 1023)
        print('Potenciômetro:', valor, '(', valor_p, '%)')
        if valor_p < 33.33:
            escala(1, 0, 0)
        elif valor_p < 66.67:
            escala(0, 1, 0)
        else:
            escala(0, 0, 1)
        sleep(1.0)
except KeyboardInterrupt:
    print('Programa finalizado')
