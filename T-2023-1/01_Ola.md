# OFC::01 Olá

Programa que realiza operações de entrada e saida de string no console (da placa), sendo executado diretamente pelo interpretador instalado na placa de desenvolvimento.

## Objetivo

Verificar a conexão adequada entre o computador e placa NodeMCU, para permitir a transferência de programas entre os dispositivos e a sua execução por meio do interpretador instalado na placa NodeMCU.

## Lista de Materiais

* Placa NodeMCU ESP8266
* Cabo USB-A -- USB-C

## Roteiro

Este roteiro não requer qualquer montagem, apenas a conexão da placa NodeMCU ao computador, pois será utilizado apenas o interpretador previamente instalado na placa de desenvolvimento e o console do IDE Thonny.

> Observe que o MicroPython já deve ter sido instalado previamente na placa NodeMCU utilizada.

1. Conecte a placa NodeMCU à porta USB de seu computador.
2. Abra o Thonny.
3. Observe se o console do interpretador Python é iniciado corretamente. Caso contrário: verifique em *Executar | Configurar interpretador* se o interpretador foi selecionado corretamente (MicroPython ESP8266) e se a porta de conexão está correta. Acione o botão *Stop* ou **CTRL+F2** para reiniciar a conexão.
4. Digite o sketch que segue na janela de edição do Thonny. (Não é necessário digitar os comentários, ou seja, as linhas iniciadas por `#`.)

```python
#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 01_Ola.py
# Entrada e saida de string no console (da placa).
#
nome = input('Qual é o seu nome? ')
print ('Olá', nome)

```

5. Salve como "01_Ola.py".
6. Para executar acione o botão *Executar* ou **F5**.

## Sugestões

* Realize a entrada de valores diferentes, em variáveis distintas.
* Converta a entrada de texto para inteiro com uso de *int()* ou real com *float()*.
* Imprima tais valores.

## Simulação

Esta [experiência](https://wokwi.com/projects/346161396802650706) pode ser simulada no [Wokwi](https://wokwi.com/projects/346161396802650706) com uso de uma placa ESP32.

---
Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2023-1
