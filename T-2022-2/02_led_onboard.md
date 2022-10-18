# OFC::02 LED onboard

Um programa que efetua o acionamento do led existente na própria placa de desenvolvimento.

## Lista de Materiais

* Placa NodeMCU ESP8266
* Cabo USB-A -- USB-C

## Roteiro

Este roteiro não requer qualquer montagem, apenas a conexão da placa NodeMCU, pois será utilizado o LED montado na própria placa (*on board*).

1. Conecte a placa NodeMCU à porta USB de seu computador.
2. Abra o Thonny.
3. Observe se o console do interpretador Python é iniciado corretamente. Caso contrário: verifique em *Executar | Configurar interpretador* se o interpretador foi selecionado corretamente (MicroPython ESP8266) e se a porta de conexão está correta. Acione o botão *Stop* ou **CTRL+F2** para reiniciar a conexão.
4. Digite o sketch que segue.

		#
		# Oficina de Computação Física
		# Prof. Peter Jandl Jr
		#
		# 02_led_onboard.py
		# Acionamento do led existente na placa.
		#
		from machine import Pin
		from time import sleep
		
		led_onboard = Pin(16, Pin.OUT)
		
		while True:
		 led_onboard.value(1)
		 sleep(0.5)
		 led_onboard.value(0)
		 sleep(2)
		  

5. Salve como "02_led_onboard.py".
6. Para executar acione o botão *Executar* ou **F5**.

Sugestões:
* Modifique a temporização do led.
* Imprima mensagens que indiquem o ponto de execução do programa.

Oficina de Computação Física | Prof. Peter Jandl Jr
2022-2