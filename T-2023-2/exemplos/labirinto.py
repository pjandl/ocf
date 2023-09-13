#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# labirinto.py
# Jogo do labirinto elétrico.
#
from machine import Pin
from time import sleep

ledVerde = Pin(13, Pin.OUT)
ledVermelho = Pin(15, Pin.OUT)

btnReset = Pin(5, Pin.IN)
trilha = Pin(16, Pin.IN)

global erros, tempoAnterior, deltaT, tomBuzzer, toque, estadoBuzzer

def reset_vars():
    erros = 0
    tempoAnterior = 0
    deltaT = 0
    tomBuzzer = 3000
    estadoBuzzer = False

def alternar(disp):
  disp.value(0)
  sleep(0.1)
  disp.value(1)
  sleep(0.5)
  disp.value(0)
  
def testa_io():
    alternar(ledVerde)
    alternar(ledVermelho)
    alternar(ledVerde)
    alternar(ledVermelho)
    

# rotina principal
print('[Labirinto] inicialização')
reset_vars()
testa_io()
print('[Labirinto] trilha ativa')

while (True):
    # verifica botão de reset
    if btnReset.value():
        reset_vars()
        testa_io()
        ledVerde.value(1)
    else:
        if trilha.value():
            sleep(0.05)
            while trilha.value():
                delay(0.
        


    