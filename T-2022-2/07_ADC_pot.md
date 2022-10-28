# OFC::07 Conversão Analógica-Digital e potenciômetro

Este programa utiliza uma entrada analógica-digital para efetuar a leitura de um potenciômetro, isto é um resistor de valor ajustável. Um potenciômetro possui três terminais: dois deles, laterais, dão acesso a sua resistência nominal (valor máximo. Seu terceiro terminal é o central e conhecido como cursor; está conectado a um botão de ajuste (rotacional ou deslizante), que permite obter uma resistência entre zero e o valor máximo do componente. Conectando os terminais laterais à alimentação, é possível obter uma tensão variável no cursor, proporcional ao valor do ajuste da resistência.

O ESP8266 possui uma única entrada analógica, no pino físico 1 (A0), na qual existe um *Analog-Digital Converter* (ADC) ou conversor analógico-digital, capaz de ler uma tensão variável na faixa de 0 a 3.3V (que é alimentação da placa), produzindo uma leitura digital na faixa de 0 a 1023 (pois o ADC interno tem resolução de 10 bits, assim 2^10 = 1024).

Esta experiência mostra o uso do ADC disponível no ESP8266, exibindo no console os valores correspondentes às leituras analógicas obtidas de um potenciômetro.

## Objetivo

Emprego de uma entrada analógica, incluindo a conversor analógico-digital correspondente, para utilização de um potênciometro como dispositivo de ajuste. 

## Lista de Materiais

* Placa NodeMCU ESP8266 (30 pinos)
* Cabo USB-A -- USB-C
* 01 Potenciômetro 10K ohms
* Jumpers

## Roteiro

Este roteiro requer uma montagem simples, além da conexão da placa NodeMCU ao computador, como na figura que segue.

![Circuito 07 ADC potenciômetro](https://github.com/pjandl/ocf/blob/main/T-2022-2/figuras/07_ADC_pot.png)

Observe que o pino físico 2 (GND) e o pino físico 10 (3V) do NodeMCU são conectados aos terminais laterais do potenciômetro. O terminal central do potenciômetro é conectado ao pino físico 1 (A0), que corresponde ao conversor ADC disponível nesta placa.

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
# 07_ADC_pot.py
# Leitura analógica de um potenciômetro, com exibição do valor no console.
#
from machine import Pin, ADC
from time import sleep

pot = ADC(0)
try:
    while True:
        valor = pot.read()
        valor_p = 100 * (valor / 1023)
        print('Potenciômetro:', valor, '(', valor_p, '%)')
        sleep(1.0)
except KeyboardInterrupt:
    print('Programa finalizado')


```

5. Salve como "07_ADC_pot.py".
6. Para executar acione o botão *Executar* ou **F5**.
7. Modifique a posição do cursor do potenciômetro, indo do início ao fim do curso possível, verificando os valores lidos e apresentados no console.

## Sugestões

* Se disponível, troque o potênciômetro por outro de valor diferente (qualquer valor entre 1K e 1M), comprovando que o funcionamento da leitura analógica.

## Simulação

Esta [experiência](https://wokwi.com/projects/346329803221107283) pode ser simulada no [Wokwi](https://wokwi.com/projects/346329803221107283) com uso de uma placa ESP32.

---

Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2022-2
