# OFC::09 Conversão Analógica-Digital, fotoresistor e escala de LEDs

Este programa utiliza uma entrada analógica-digital para efetuar a leitura de um *fotoresistor* ou *light dependant resistor* (LDR), ou seja, um resistor variável conforme a luminosidade detectada. O LDR possui dois terminais, sem polaridade e, em geral, sua resistência é tanto menor quanto maior a luminosidade recebida. O LDR será montado em série com um resistor de valor fixo, criando um divisor de tensão, cuja tensão variável tem relação com a luminosidade. A junção do LDR e do resistor será conectada a entrada analógica do ESP8266.

O ESP8266 possui única uma entrada analógica, no pino físico 1 (A0), na qual existe um *Analog-Digital Converter* (ADC) ou conversor analógico-digital, capaz de ler uma tensão variável na faixa de 0 a 3.3V (que é alimentação da placa), produzindo uma leitura digital na faixa de 0 a 1023 (pois o ADC interno tem resolução de 10 bits, assim 2^10 = 1024).

Esta experiência mostra o uso do ADC disponível no ESP8266, exibindo a luminosidade detectada pelo LDR numa escala de leds coloridos.

## Objetivo

Emprego de uma entrada analógica, incluindo a conversor analógico-digital correspondente, para utilização de um sensor analógico de luminosidade, apresentando o resultado numa escala de leds (uso de saídas digitais).

## Lista de Materiais

* Placa NodeMCU ESP8266 (30 pinos)
* Cabo USB-A -- USB-C
* 01 Fotoresistor LDR (GL5528)
* 01 Resistor 10K ohms (marron-preto-laranja)
* 03 Leds (vermelho, branco, verde)
* 03 Resistores 330 ohms (laranja-laranja-marrom)
* Jumpers

## Roteiro

Este roteiro requer uma montagem simples, além da conexão da placa NodeMCU ao computador, como na figura que segue.

![Circuito 09 ADC ldr leds](https://github.com/pjandl/ocf/blob/main/T-2022-2/figuras/09_ADC_ldr_leds.png)

O pino físico 10 (3V) do NodeMCU é ligado à um dos terminais do fotoresistor (que não tem polaridade). O outro terminal do fotoresistor forma uma junção com um dos terminais do resistor de 10K e o pino físico 1 (A0), que corresponde à entrada do conversor ADC disponível nesta placa. O segundo terminal do resistor de 10K é ligado ao terra, ou seja, ao pino físico 2 (GND).

O pino físico 20 (D8 -> GPIO15) é conectado ao ânodo do led vermelho. O pino físico 21 (D7 -> GPIO13) é conectado ao ânodo do led branco. O pino físico 22 (D6 -> GPIO12) é conectado ao ânodo do led verde. Um terminal de cada resistor de 330 ohms deve ser conectado aos cátodos dos led e o outro terminal ao terra (pino físico 24 -> GND, ou outro equivalente).

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
# 09_ADC_ldr_leds.py
# Leitura analógica de um fotoresistor (LDR), com exibição numa escala de leds.
#
from machine import Pin, ADC
from time import sleep

ldr = ADC(0)
leds = [
    Pin(12, Pin.OUT),
    Pin(13, Pin.OUT),
    Pin(15, Pin.OUT)
    ]

def mapear_escala(valor, min, max, faixas):
    valor_p = (valor - min) / (max - min)
    print('valor:', valor, '(', 100*valor_p, '%)', end=' ')
    for n_led in range(len(leds)):
        estado = valor_p > (n_led + 1) / faixas
        leds[n_led].value(estado)
        print(n_led, ':', estado, '|', end=' ')
    print()
    
try:
    while True:
        valor = ldr.read()
        mapear_escala(valor, 0, 1023, 4)
        sleep(2.0)
except KeyboardInterrupt:
    print('Programa finalizado')

```

5. Salve como "09_ADC_ldr_leds.py".
6. Para executar acione o botão *Executar* ou **F5**.
7. Modifique a incidência de luz no LDR (cobrindo-o e usando uma lanterna), verificando o acendimento dos leds, conferindo com os valores apresentados no console.

## Sugestões

* Modifique a montagem e o programa que um led seja aceso quando a luminosidade estiver abaixo de um valor específico (por exemplo, quando `valor < 500`.

## Simulação

Esta [experiência](https://wokwi.com/projects/346334549714666068) pode ser simulada no [Wokwi](https://wokwi.com/projects/346334549714666068) com uso de uma placa ESP32.

---

Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2022-2
