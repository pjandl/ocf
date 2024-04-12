#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 07_ADC_pot.py
# Leitura analógica de um potenciômetro, com exibição do
# valor no console.
#
from machine import Pin, ADC
from time import sleep

# potenciômetro conectado ao pino 1 (ADC0)
pot = ADC(0)
try:
    while True:
        valor = pot.read()
        valor_p = 100 * (valor / 1023)
        print('Potenciômetro:', valor, '(', round(valor_p, 4), '%)')
        sleep(1.0)
except KeyboardInterrupt:
    print('Programa finalizado')
