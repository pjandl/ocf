#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 10_ADC_ntc.py
# Leitura analógica de um termistor (NTC), com led de alerta
# para temperatura alta.
#
from machine import Pin, ADC
from math import log
from time import sleep

# termistor conectado ao pino 1 (ADC0)
ntc = ADC(0)
# saida conectada ao led externo
led = Pin(15, Pin.OUT)

def temperatura(resolucao=1023):
    tempK = log(10000.0 * (resolucao / ntc.read() - 1))
    tempK = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * tempK * tempK)) * tempK)
    return tempK
    
def K_para_C(K):
  return K - 273.15

try:
    while True:
        temp = temperatura()
        print("Temperatura:", round(temp, 2), "K |",
              round(K_para_C(temp), 2), "˚C")
        if temp > 300:
            led.on()
            print("Alerta de temperatura!!")
        else:
            led.off()
        sleep(4.0)
except KeyboardInterrupt:
    print('Programa finalizado')
