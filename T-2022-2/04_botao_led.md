# OFC::04 Botão e LED

Um programa monitora o estado de um botão (*chave táctil*), de modo que seu acionamento liga o led montado externamente à placa de desenvolvimento. O led permanece aceso enquanto o botão é acionado/pressionado. Mostra o uso de porta GPIO (*General Purpose Input Output*) como entrada digital ou como uma saída digital.

## Lista de Materiais

* Placa NodeMCU ESP8266 (30 pinos)
* Cabo USB-A -- USB-C
* 01 Led (qualquer cor)
* 01 Chave táctil
* 01 Resistor 220 ou 330 ohms
* 01 Resistor 10K ohms
* Jumpers

## Roteiro

Este roteiro requer uma montagem simples, além da conexão da placa NodeMCU ao computador, como na figura que segue.

Observe que o pino físico 20 (D8) do NodeMCU, que corresponde a GPIO15, será conectado ao ânodo do led (terminal positivo, mais longo). O cátodo do led (terminal negativo, mais curto) será conectado ao resistor (não tem polaridade), de maneira que fiquem em série. O outro terminal do resistor deve ser ligado ao pino físico 17 GND (*ground*) do NodeMCU, que é o terra do circuito.

O pino físico 22 (D6) do NodeMCU, que corresponde a GPIO12, será conectada à chave tactil, do mesmo lado que o resistor de 10K, o qual é conectado ao terra (pino físico 17 GND). O outro lado da chave táctil deve ser ligado ao pino físico 16 3V (alimentação de 3.3 Volts fornecida pela placa). Esta configuração de ligação do resistor na chave táctil é conhecida como *pull down*, pois quando a chave não estiver acionada, fornecerá um valor 0 (zero lógico ou *False*); quando acionada fornecerá o valor da alimentação (um lógico ou *True*).

1. Efetue a montagem indicada. Confira todas as conexões.
2. Conecte a placa NodeMCU à porta USB de seu computador.
3. Abra o Thonny.
4. Observe se o console do interpretador Python é iniciado corretamente. Caso contrário: verifique em *Executar | Configurar interpretador* se o interpretador foi selecionado corretamente (MicroPython ESP8266) e se a porta de conexão está correta. Acione o botão *Stop* ou **CTRL+F2** para reiniciar a conexão.
5. Digite o sketch que segue.

```python
#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 04_botao_led.py
# Um botão para acionamento do led externo.
#
from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT)
botao = Pin(12, Pin.IN)

try:
	while True:
		led.value(botao.value())
		sleep(0.1)
except KeyboardInterrupt:
	led.value(0)
	print('Programa finalizado')
		  
```

5. Salve como "04_botao_led.py".
6. Para executar acione o botão *Executar* ou **F5**.
7. Acione o botão e verifique o acendimento do led.

## Sugestões

* Modifique a temporização do laço e verique o comportamento do circuito.
* inclua um *if/else* de maneira que possam ser impressas mensagens quando o led é aceso ou apagado.

## Simulação

Esta [experiência](https://wokwi.com/projects/346164150480667220) pode ser simulada no [Wokwi](https://wokwi.com/projects/346164150480667220) com uso de uma placa ESP32.

---

Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2022-2
