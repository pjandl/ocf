# OFC::00 Hello World

Um programa clássico executado diretamente pelo interpretador instalado na placa de desenvolvimento.

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
		# 00_Hello_World.py
		# Um clássico executado na placa de desenvolvimento!
		#
		import sys

		message = 'Hello World, from micro Python'
		print(message)

		impl = sys.implementation
		print(f'{impl.name} v{impl.version[0]}.{impl.version[1]}')


5. Salve como "00_Hello_World.py".
6. Para executar acione o botão *Executar* ou **F5**.

## Sugestões

* Modifique a mensagem e execute novamente.
* Imprima várias mensagens diferentes.

### Simulação

Esta [https://wokwi.com/projects/345887141617730130](experiência) pode ser simulada no [https://wokwi.com/projects/345887141617730130](Wokwi).

---

Oficina de Computação Física | Prof. Peter Jandl Jr
2022-2
