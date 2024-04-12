# OFC::04 Botão e LED

Um programa monitora o estado de um botão (*chave táctil*), de modo que seu acionamento liga o led montado externamente à placa de desenvolvimento. O led permanece aceso enquanto o botão é acionado/pressionado. Mostra o uso de porta GPIO (*General Purpose Input Output*) como entrada digital ou como uma saída digital.

## Objetivo

Configuração e uso de uma entrada digital, conectada à um botão; e uma saída digital, conectada à um led; mostrando o controle direto de dispositivos externos ao NodeMCU.

## Lista de Materiais

* Placa NodeMCU ESP8266 (30 pinos)
* Cabo USB-A -- micro-USB
* 01 Led (qualquer cor)
* 01 Chave táctil (*push button*)
* 01 Resistor 220 ohms (vermelho-vermelho-marron) ou 330 ohms (laranja-laranja-marrom)
* 01 Resistor 10K ohms (marron-preto-laranja)
* Jumpers

> Observe que o MicroPython já deve ter sido instalado previamente na placa NodeMCU utilizada.

## Roteiro

Este roteiro requer uma montagem simples, além da conexão da placa NodeMCU ao computador, como na figura que segue.

![Circuito 04 botão led](https://github.com/pjandl/ocf/blob/main/T-2023-2/figuras/04_botao_led.png)

> Esta montagem cria um circuito elétrico, ou seja, um caminho para a circulação de corrente elétrica. O pino do NodeMCU usado como saída fornece uma corrente elétrica, que deve fluir; entrando pelo ânodo do led e saindo pelo seu cátodo; entrando por um terminal do resistor e saindo por outro, retornando ao NodeMCU por meio do seu terra (*ground*).
> O outro circuito elétrico constuído nesta montagem usa um pino do NodeMCU como entrada, ou seja, recebe uma corrente elétrica. Quando a chave táctil não está pressionada, a entrada não recebe qualquer corrente, pois a chave apenas conecta o resistor, que está ligado ao terra, à entrada, sendo interpretada como um valor lógico *False*. Quando a chave tácil é pressionada, a alimentação (*Vcc*) é conectada à entrada do NodeMCU, provendo circulação de corrente, interpretada como um valor lógico *True*.

Observe que o pino físico 20 (D8) do NodeMCU, que corresponde a GPIO15, será conectado ao ânodo do led (terminal positivo, mais longo). O cátodo do led (terminal negativo, mais curto) será conectado ao resistor (não tem polaridade), de maneira que fiquem em série. O outro terminal do resistor deve ser ligado ao pino físico 17 GND (*ground*) do NodeMCU, que é o terra do circuito.

O pino físico 23 (D5) do NodeMCU, que corresponde a GPIO14, será conectada à chave tactil, do mesmo lado que o resistor de 10K, o qual é conectado ao terra (pino físico 17 GND). O outro lado da chave táctil deve ser ligado ao pino físico 16 3V (alimentação de 3.3 Volts fornecida pela placa). Esta configuração de ligação do resistor na chave táctil é conhecida como *pull down*, pois quando a chave não estiver acionada, fornecerá um valor 0 (zero lógico ou *False*); quando acionada fornecerá o valor da alimentação (um lógico ou *True*).

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
botao = Pin(14, Pin.IN)

try:
	while True:
		led.value(botao.value())
		sleep(0.1)
except KeyboardInterrupt:
	led.value(0)
	print('Programa finalizado')
		  
```

6. Salve como "04_botao_led.py".
7. Para executar acione o botão *Executar* ou **F5**.
8. Acione o botão e verifique o acendimento do led.

## Sugestões

* Modifique a temporização do laço e verique o comportamento do circuito.
* inclua um *if/else* de maneira que possam ser impressas mensagens quando o led é aceso ou apagado.
* acrescente um buzzer para emitir um sinal sonoro junto do acendimento do led, usando, por exemplo, o sketch que segue.

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
botao = Pin(14, Pin.IN)

try:
	while True:
		led.value(botao.value())
		sleep(0.1)
except KeyboardInterrupt:
	led.value(0)
	print('Programa finalizado')
		  
```

## Simulação

Esta [experiência](https://wokwi.com/projects/346164150480667220) pode ser simulada no [Wokwi](https://wokwi.com/projects/346164150480667220) com uso de uma placa ESP32.

---

Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2024-1
