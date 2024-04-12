# OFC::10 Conversão Analógica-Digital, termistor e LED

Este programa utiliza uma entrada analógica-digital para efetuar a leitura de um *termistor*, ou seja, um resistor variável conforme a temperatura detectada. O termistor possui dois terminais, sem polaridade, e funciona de duas maneiras:

- *Positive Temperature Coeficient* (PTC), quando sua resistência aumenta conforme a temperatura aumenta; 
- *Negative Temperature Coeficient* (NTC), quando sua resistência diminui conforme a temperatura aumenta.

Nesta experiência usaremos um NTC que será montado em série com um resistor de valor fixo, criando um divisor de tensão, cuja tensão variável tem relação com a temperatura. A junção do NTC e do resistor será conectada a entrada analógica do ESP8266.

O ESP8266 possui única uma entrada analógica, no pino físico 1 (A0), na qual existe um *Analog-Digital Converter* (ADC) ou conversor analógico-digital, capaz de ler uma tensão variável na faixa de 0 a 3.3V (que é alimentação da placa), produzindo uma leitura digital na faixa de 0 a 1023 (pois o ADC interno tem resolução de 10 bits, assim 2^10 = 1024).

Esta experiência mostra o uso do ADC disponível no ESP8266, exibindo a temperatura detectada pelo NTC e também um led para alerta quando a temperatura for superior a 27˚C.

## Objetivo

Emprego de uma entrada analógica, incluindo o conversor analógico-digital correspondente, para utilização de um transdutor de temperatura (termistor NTC), com uso de um led de alerta para temperatura acima de um limiar (com uso de saída digital).

## Lista de Materiais

* Placa NodeMCU ESP8266 (30 pinos)
* Cabo USB-A -- micro-USB
* 01 Termistor NTC 10K
* 01 Resistor 10K ohms (marron-preto-laranja)
* 01 Led vermelho
* 01 Resistor 330 ohms (laranja-laranja-marrom)
* Jumpers

## Roteiro

Este roteiro requer uma montagem simples, além da conexão da placa NodeMCU ao computador, como na figura que segue.

![Circuito 10 ADC NTC](https://github.com/pjandl/ocf/blob/main/T-2023-2/figuras/10_ADC_ntc.png)

O pino físico 10 (3V3) do NodeMCU é conectado a um dos terminais do termistor NTC, que não tem polaridade. O segundo terminal do termistor NTC forma uma junção com o resistor de 10K e uma conexão ao pino físico 1 (A0), que corresponde ao conversor ADC disponível nesta placa. O outro terminal do resistor de 10K deve ser conectado ao terra (pino físico 2 -> GND, ou outro equivalente).

O pino físico 20 (D8 -> GPIO15) é conectado ao ânodo do led vermelho. O cátodo do led deve ser conectado a um dos terminais resistor de 330 ohms e o outro terminal ao terra (pino físico 2 -> GND).

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
# 10_ADC_ntc.py
# Leitura analógica de um termistor (NTC), com led de alerta
# para temperatura alta.
#
from machine import Pin, ADC
from math import log
from time import sleep

# termistor conectado ao pino 1 (ADC0)
ntc = ADC(0)
# saida conectada ao led externo
led = Pin(15, Pin.OUT)

def temperatura(resolucao=1023):
    tempK = log(10000.0 * (resolucao / ntc.read() - 1))
    tempK = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * tempK * tempK)) * tempK)
    return tempK
    
def K_para_C(K):
  return K - 273.15

try:
    while True:
        temp = temperatura()
        print("Temperatura:", round(temp, 2), "K |",
              round(K_para_C(temp), 2), "˚C")
        if temp > 300: # 300 K = 26.85°C
            led.on()
            print("Alerta de temperatura!!")
        else:
            led.off()
        sleep(4.0)
except KeyboardInterrupt:
    print('Programa finalizado')

```

6. Salve como "10_ADC_ntc.py".
7. Para executar acione o botão *Executar* ou **F5**.
8. Modifique temperatura no NTC segurando-o , verificando o acendimento do led de alerta e dos valores apresentados no console.

## Sugestões

* Altere o programa para o led seja aceso para outra temperatura.
* Modifique a montagem para acrescentar um segundo led (p.e., azul), que seja ativado quando a temperatura é menor do que 20˚C.

## Simulação

Esta [experiência](https://wokwi.com/projects/346510631510213204) pode ser simulada no [Wokwi](https://wokwi.com/projects/346510631510213204) com uso de uma placa ESP32.

---

Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2023-2
