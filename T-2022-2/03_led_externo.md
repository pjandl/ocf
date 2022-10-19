# OFC::03 LED externo

Um programa que efetua o acionamento de um led montado externamente à placa de desenvolvimento. Mostra o uso de uma porta GPIO (*General Purpose Input Output*) como uma saída digital.

## Lista de Materiais

* Placa NodeMCU ESP8266 (30 pinos)
* Cabo USB-A -- USB-C
* 01 Led (qualquer cor)
* 01 Resistor 220 ou 330 ohms

## Roteiro

Este roteiro requer uma montagem simples, além da conexão da placa NodeMCU ao computador, como na figura que segue.

Observe que o pino 20 do NodeMCU, sua GPIO15, será conectado ao ânodo do led (terminal positivo, mais longo). O cátodo do led (terminal negativo, mais curto) será conectado ao resistor (não tem polaridade), de maneira que fiquem em série. O outro terminal do resistor deve ser ligado ao pino 17 do NodeMCU, que é seu GND (*ground*) -- terra do circuito.  

1. Efetue a montagem indicada. Confira todas as conexões.
2. Conecte a placa NodeMCU à porta USB de seu computador.
3. Abra o Thonny.
4. Observe se o console do interpretador Python é iniciado corretamente. Caso contrário: verifique em *Executar | Configurar interpretador* se o interpretador foi selecionado corretamente (MicroPython ESP8266) e se a porta de conexão está correta. Acione o botão *Stop* ou **CTRL+F2** para reiniciar a conexão.
5. Digite o sketch que segue.

		#
		# Oficina de Computação Física
		# Prof. Peter Jandl Jr
		#
		# 03_led_externo.py
		# Acionamento do led existente na placa.
		#
		from machine import Pin
		from time import sleep
		
		led_onboard = Pin(15, Pin.OUT)
		
		while True:
		 led_onboard.value(1)
		 sleep(0.5)
		 led_onboard.value(0)
		 sleep(2.0)
		  

5. Salve como "03_led_externo.py".
6. Para executar acione o botão *Executar* ou **F5**.

Sugestões:
* Modifique a temporização do led.
* Imprima mensagens que indiquem o ponto de execução do programa.

Oficina de Computação Física | Prof. Peter Jandl Jr
2022-2
