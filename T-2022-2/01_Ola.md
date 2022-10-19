# OFC::01 Olá

Programa que realiza operações de entrada e saida de string no console (da placa), sendo executado diretamente pelo interpretador instalado na placa de desenvolvimento.

## Lista de Materiais

* Placa NodeMCU ESP8266
* Cabo USB-A -- USB-C

## Roteiro

Este roteiro não requer qualquer montagem, apenas a conexão da placa NodeMCU ao computador, pois será utilizado apenas o interpretador previamente instalado na placa de desenvolvimento e o console do IDE Thonny.

1. Conecte a placa NodeMCU à porta USB de seu computador.
2. Abra o Thonny.
3. Observe se o console do interpretador Python é iniciado corretamente. Caso contrário: verifique em *Executar | Configurar interpretador* se o interpretador foi selecionado corretamente (MicroPython ESP8266) e se a porta de conexão está correta. Acione o botão *Stop* ou **CTRL+F2** para reiniciar a conexão.
4. Digite o sketch que segue.

		#
		# Oficina de Computação Física
		# Prof. Peter Jandl Jr
		#
		# 01_Ola.py
		# Entrada e saida de string no console (da placa).
		#
		nome = input('Qual é o seu nome? ')
		print ('Olá', nome)
		

5. Salve como "01_Ola.py".
6. Para executar acione o botão *Executar* ou **F5**.

Sugestões:
* Realize a entrada de valores diferentes, em variáveis distintas.
* Converta a entrada de texto para inteiro com uso de *int()* ou real com *float()*.
* Imprima tais valores.

Oficina de Computação Física | Prof. Peter Jandl Jr
2022-2
