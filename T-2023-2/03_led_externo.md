# OFC::03 LED externo

Um programa que efetua o acionamento de um led montado externamente à placa de desenvolvimento. Mostra o uso de uma porta GPIO (*General Purpose Input Output*) como uma saída digital.

## Objetivo

Configuração e uso de uma saída digital, que pode ser utilizada para controlar dispositivos externos ao NodeMCU (no caso um led).

## Lista de Materiais

* Placa NodeMCU ESP8266 (30 pinos)
* Cabo USB-A -- USB-C
* 01 Led (qualquer cor)
* 01 Resistor 220 ohms (vermelho-vermelho-marron) ou 330 ohms (laranja-laranja-marrom)
* Jumpers

> Observe que o MicroPython já deve ter sido instalado previamente na placa NodeMCU utilizada.

## Roteiro

Este roteiro requer uma montagem simples, além da conexão da placa NodeMCU ao computador, como na figura que segue. Aqui um led é conectado a uma saída do NodeMCU, que controla seu acendimento. O resistor, montado em série ao led, é usado para limitar a corrente elétrica fornecida pela placa NodeMCU e que passa pelo led, evitando danificar tais componentes. 

![Circuito 03 led externo](https://github.com/pjandl/ocf/blob/main/T-2023-2/figuras/03_led_externo.png)

> Esta montagem cria um circuito elétrico, ou seja, um caminho para a circulação de corrente elétrica. O pino do NodeMCU usado como saída fornece uma corrente elétrica, que deve fluir; entrando pelo ânodo do led e saindo pelo seu cátodo; entrando por um terminal do resistor e saindo por outro, retornando ao NodeMCU por meio do seu terra (*ground*).

Observe que o pino físico 20 (D8) do NodeMCU, que corresponde a GPIO15, será conectado ao ânodo do led (terminal positivo, mais longo). O cátodo do led (terminal negativo, mais curto) será conectado ao resistor (não tem polaridade), de maneira que fiquem em série. O outro terminal do resistor deve ser ligado ao pino físico 17 GND (*ground*) do NodeMCU, que é o terra do circuito.  

1. Efetue a montagem indicada. Confira todas as conexões.
2. Conecte a placa NodeMCU à porta USB de seu computador.
3. Abra o Thonny.
4. Observe se o console do interpretador Python é iniciado corretamente. Caso contrário: verifique em *Executar | Configurar interpretador* se o interpretador foi selecionado corretamente (MicroPython ESP8266) e se a porta de conexão está correta. Acione o botão *Stop* ou **CTRL+F2** para reiniciar a conexão.
5. Digite o sketch que segue na janela de edição do Thonny. (Não é necessário digitar os comentários, ou seja, as linhas iniciadas por `#`.)

```python
#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 03_led_externo.py
# Acionamento do led externo à placa.
#
from machine import Pin
from time import sleep

led1 = Pin(15, Pin.OUT)

while True:
    led1.value(1)
    sleep(0.5)
    led1.value(0)
    sleep(0.5)

```

6. Salve como "03_led_externo.py".
7. Para executar acione o botão *Executar* ou **F5**.

## Sugestões

* Modifique a temporização do led, aumentando ou diminuindo os valores usados na função `sleep`.
* Imprima mensagens que indiquem o ponto de execução do programa.
* Acrescente na montagem, um segundo led, de qualquer cor, com outro resistor de mesmo valor, mas conectando em outra saída do NodeMCU (por exemplo, pino físico 21 (D7) ou GPIO13). Veja as modificações neste outro sketch:

```python
#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 03_dois_leds_externos.py
# Acionamento dos leds externos à placa.
#
from machine import Pin
from time import sleep

led1 = Pin(15, Pin.OUT)
led2 = Pin(13, Pin.OUT)

while True:
    led1.value(1)
    sleep(0.5)
    led1.value(0)
    sleep(0.5)
    led2.value(1)
    sleep(0.5)
    led2.value(0)
    sleep(0.5)

```

## Simulação

Esta [experiência](https://wokwi.com/projects/346163718014370386) pode ser simulada no [Wokwi](https://wokwi.com/projects/346163718014370386) com uso de uma placa ESP32.

---
Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2023-2
