# OFC::02 LED onboard

Um programa que efetua o acionamento do led existente na própria placa de desenvolvimento.

## Objetivo

Utilizar elementos básicos da programação de dispositivos microprocessados.

## Lista de Materiais

* Placa NodeMCU ESP8266
* Cabo USB-A -- USB-C

## Roteiro

Este roteiro não requer qualquer montagem, apenas a conexão da placa NodeMCU ao computador, pois será utilizado o interpretador previamente instalado na placa de desenvolvimento e o LED montado na própria placa (*on board*).

1. Conecte a placa NodeMCU à porta USB de seu computador.
2. Abra o Thonny.
3. Observe se o console do interpretador Python é iniciado corretamente. Caso contrário: verifique em *Executar | Configurar interpretador* se o interpretador foi selecionado corretamente (MicroPython ESP8266) e se a porta de conexão está correta. Acione o botão *Stop* ou **CTRL+F2** para reiniciar a conexão.
4. Digite o sketch que segue.

```python
#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 02_led_onboard.py
# Acionamento do led existente na placa.
#
# O led onboard do ESP8266 é ativado em baixo, com value(0) ou off(),
# e desligado com value(1) ou on().		
#
from machine import Pin
from time import sleep

led_onboard = Pin(2, Pin.OUT)

while True:
	led_onboard.value(0)
	sleep(0.5)
	led_onboard.value(1)
	sleep(2.0)

```

5. Salve como "02_led_onboard.py".
6. Para executar acione o botão *Executar* ou **F5**.

## Sugestões

* Modifique a temporização do led.
* Imprima mensagens que indiquem o ponto de execução do programa.

## Simulação

Esta [experiência](https://wokwi.com/projects/345887313822220884) pode ser simulada no [Wokwi](https://wokwi.com/projects/345887313822220884) com uso de uma placa ESP32.

---

Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2022-2
