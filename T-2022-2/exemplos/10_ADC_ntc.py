#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 10_ADC_ntc.py
# Leitura analógica de um termistor (NTC), com led de alerta para temperatura alta.
#
from machine import Pin, ADC
from math import log
from time import sleep

ntc = ADC(0)
BETA = 3950 # correspondente ao termistor usado
led = Pin(15, Pin.OUT)

def temperatura(valor_bruto):
    tempK = 1 / (log(1 / (1023. / valor_bruto - 1)) / BETA + 1.0 / 298.15)
    tempC = tempK - 273.15
    return tempK, tempC

try:
    while True:
        leitura = ntc.read()
        temp = temperatura(leitura)
        print("Temperatura:",
              round(temp[0], 2), "K |",
              round(temp[1], 2), "˚C")
        if temp[1] > 27:
            led.on()
            print("Alerta de temperatura")
        else:
            led.off()
        sleep(4.0)
except KeyboardInterrupt:
    print('Programa finalizado')
