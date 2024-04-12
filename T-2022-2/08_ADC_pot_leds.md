# OFC::08 Conversão Analógica-Digital, potenciômetro e escala de LEDs

Este programa utiliza uma entrada analógica-digital para efetuar a leitura de um potenciômetro, isto é um resistor de valor ajustável. Um potenciômetro possui três terminais: dois deles, laterais, dão acesso a sua resistência nominal (valor máximo. Seu terceiro terminal é o central e conhecido como cursor; está conectado a um botão de ajuste (rotacional ou deslizante), que permite obter uma resistência entre zero e o valor máximo do componente. Conectando os terminais laterais à alimentação, é possível obter uma tensão variável no cursor, proporcional ao valor do ajuste da resistência.

O ESP8266 possui uma única entrada analógica, no pino físico 1 (A0), na qual existe um *Analog-Digital Converter* (ADC) ou conversor analógico-digital, capaz de ler uma tensão variável na faixa de 0 a 3.3V (que é alimentação da placa), produzindo uma leitura digital na faixa de 0 a 1023 (pois o ADC interno tem resolução de 10 bits, assim 2^10 = 1024).

Esta experiência mostra o uso do ADC disponível no ESP8266, exibindo numa escala de leds coloridos (e no console) os valores correspondentes às leituras analógicas obtidas de um potenciômetro.

## Objetivo

Emprego de uma entrada analógica, incluindo a conversor analógico-digital correspondente, para utilização de um potênciometro como dispositivo de ajuste de uma escala de três leds.

## Lista de Materiais

* Placa NodeMCU ESP8266 (30 pinos)
* Cabo USB-A -- micro-USB
* 01 Potenciômetro 10K ohms
* 03 Leds (vermelho, branco, verde)
* 03 Resistores 330 ohms (laranja-laranja-marrom)
* Jumpers

## Roteiro

Este roteiro requer uma montagem simples, além da conexão da placa NodeMCU ao computador, como na figura que segue.

![Circuito 08 ADC pot leds](https://github.com/pjandl/ocf/blob/main/T-2022-2/figuras/08_ADC_pot_leds.png)

Observe que o pino físico 2 (GND) e o pino físico 10 (3V) do NodeMCU são conectados aos terminais laterais do potenciômetro. O terminal central do potenciômetro é conectado ao pino físico 1 (A0), que corresponde ao conversor ADC disponível nesta placa.

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
# 08_ADC_pot_leds.py
# Leitura analógica de um potenciômetro, com exibição numa escala de leds.
#
from machine import Pin, ADC
from time import sleep

pot = ADC(0)
ledVerd = Pin(12, Pin.OUT)
ledBran = Pin(13, Pin.OUT)
ledVerm = Pin(15, Pin.OUT)

def escala(verde, branco, vermelho):
    ledVerd.value(verde)
    ledBran.value(branco)
    ledVerm.value(vermelho)
    
try:
    while True:
        valor = pot.read()
        valor_p = 100 * (valor / 1023)
        print('Potenciômetro:', valor, '(', valor_p, '%)')
        if valor_p < 33.33:
            escala(1, 0, 0)
        elif valor_p < 66.67:
            escala(0, 1, 0)
        else:
            escala(0, 0, 1)
        sleep(1.0)
except KeyboardInterrupt:
    print('Programa finalizado')

```

6. Salve como "08_ADC_pot_leds.py".
7. Para executar acione o botão *Executar* ou **F5**.
8. Modifique a posição do cursor do potenciômetro, indo do início ao fim do curso possível, verificando o acendimento dos leds correspondentes à cada faixa, conferindo com os valores apresentados no console.

## Sugestões

* Modifique o programa para que existam cinco faixas: [0 a 204] led verde; [205 a 409] led verde e led branco; [410 a 614] led branco; [615 a 819] led branco e led vermelho; [819 a 1024] led vermelho.

## Simulação

Esta [experiência](https://wokwi.com/projects/346332996795630163) pode ser simulada no [Wokwi](https://wokwi.com/projects/346332996795630163) com uso de uma placa ESP32.

---

Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2022-2
