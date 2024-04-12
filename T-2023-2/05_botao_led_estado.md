# OFC::05 Botão com retenção de estado e LED

Um programa que monitora o estado de um botão (*chave táctil*), de modo que seu acionamento alterna o funcionamento do led montado externamente à placa de desenvolvimento, cujo estado é mantido. Quando o botão é acionado ocorre a troca de estado do led: se o led está desligado, um acionamento do botão liga o led, que permanece aceso até que o botão seja pressionado novamente. Mostra o uso de porta GPIO (*General Purpose Input Output*) como entrada digital ou como uma saída digital, além de variáveis para retenção de estado.

A montagem é a mesma que a proposta na experiência anterior (04 Botão e LED).

## Objetivo

Configuração e uso de uma entrada digital, conectada à um botão; e uma saída digital, conectada à um led; mostrando o controle de dispositivos externos ao NodeMCU com retenção de estado.

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

![Circuito 05 botão led](https://github.com/pjandl/ocf/blob/main/T-2023-2/figuras/05_botao_led_estado.png)

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
# 05_botao_led_estado.py
# Um botão, com manutenção de estado, para acionamento do led externo.
#
from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT)
botao = Pin(14, Pin.IN)
estado = 0
ultimo = 0
try:
    while True:
        valor = botao.value()
        if valor == 1 and ultimo == 0:
            estado = not estado
            led.value(estado)
        ultimo = valor
        sleep(0.2)
except KeyboardInterrupt:
    led.value(0)
    print('Programa finalizado')
		  
```

6. Salve como "05_botao_led_estado.py".
7. Para executar acione o botão *Executar* ou **F5**.
8. Acione o botão e verifique o acendimento do led e a retenção de seu estado.

## Sugestões

* Adicione um segundo led, de maneira que existam três estados sequenciais de funcionamento: tudo desligado, um led ligado, dois leds ligados, tudo desligado e assim sucessivamente.
* Modifique a sequência para que seja: tudo desligado, um led ligado, dois leds ligados, um led ligado, tudo desligado, repetindo o ciclo.

## Simulação

Esta [experiência](https://wokwi.com/projects/346254975009030738) pode ser simulada no [Wokwi](https://wokwi.com/projects/346254975009030738) com uso de uma placa ESP32.

---

Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2023-2
