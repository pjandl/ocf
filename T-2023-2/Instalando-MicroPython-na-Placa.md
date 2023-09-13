# Instalando o MicroPython nas Placas de Desenvolvimento

Nos roteiros desenvolvidos nesta oficina, escolhemos o Python como linguagem de programação para controlarmos as placas de desenvolvimento utilizadas nos protótipos construídos. Esta linguagem foi escolhida por três razões: sua simplicidade permite uma aprendizagem mais rápida; é uma das preferidas tanto no âmbito acadêmico, como no mercado comercial de programação; possui uma enorme biblioteca de módulos que agilizam o desenvolvimento de soluções.

MicroPython é uma implementação de software muito compatível com a linguagem de programação Python 3, escrita em C e otimizada para ser executadas em um microcontrolador. É composta de um compilador Python para bytecode e um interpretador desse bytecode capaz de executar programas escritos em Python em placas de desenvolvimento específicas.

## Objetivo

Efetuar a instalação do *firmware* MicroPython em uma placa de desenvolvimento, possibilitando sua utilização na prototipagem de soluções de computação física (e também internet das coisas).

## Lista de Materiais

* Placa NodeMCU ESP8266 ou ESP32
* Cabo USB-A -- USB-C

## Roteiro

Este roteiro não requer qualquer montagem, apenas a conexão da placa NodeMCU ao computador, possibilitando a instalação do *firmware* MicroPython na placa de desenvolvimento com uso do IDE Thonny.

## Instalação do Thonny

O IDE Thonny é um ambiente de desenvolvimento integrado para Python, que integra um editor de programas, um console para execução dos programas e um depurador; o que torna o trabalho de programar mais simples. Além disso, permite a conexão com várias placas de desenvolvimento, além de executar a instalação do *firmware* MicroPython nestas placas.

1. Faça o *download* do IDE Thonny em [https://thonny.org/](https://thonny.org/). Selecione a versão adequada ao seu sistema operacional. A versão *Installer with 64-bit Python 3.10* é bastante conveniente.
2. Execute o instalador, aceite a licensa e escolha as opções de instalação que julgar adequadas em relação ao diretório de instalação, idioma e criação de atalhos.
3. Execute o Thonny.
![IDE Thonny](https://github.com/pjandl/ocf/blob/main/T-2023-1/figuras/thonny_ide_1.png)
4. Copie o código que segue na área de edição do Thonny.
```python
# Prof. Peter Jandl Jr
#
# teste.py
# Programa de teste do IDE Thonny.
#
import sys

msg = 'Oficina do Python'
print('Bem-vindo')
for a in range(3):
    print(msg)
print(sys.implementation.name)

```
5. Salve o programa com **Ctrl+S**. Use o nome "teste.py".
6. Execute o programa com  **F5**. O resultado deve ser como segue.
![Execução de programa no IDE Thonny](https://github.com/pjandl/ocf/blob/main/T-2023-1/figuras/thonny_ide_2.png)

## Instalação do Driver Serial

Para que o Thonny possa se conectar à placa de desenvolvimento por meio da porta USB do computador, usualmente é necessário instalar um *device driver* de comunicação serial, ou seja, um módulo de software que permitirá a comunicação computador-placa.

1. Faça o *download* do *device driver* adequado.
* Placas NodeMCU V3 ou ESP8266 geralmente requere o driver "CH340G", cuja versão para Windows pode ser obtida [aqui](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CH341SER_WINDOWS.zip).
* Placas NodeMCU V2 ou ESP32 geralmente requere o driver "CP210x", cuja versão para Windows pode ser obtida [aqui](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CP210x_Windows_Drivers.zip).
2. Descompacte o arquivo e execute o instalador.
3. Acione *Install* ou *Next* e depois *Ok* ou *Finish* quando a instalação for confirmada.

Isto permite a comunicação do Thonny com a placa de desenvolvimento escolhida.

Maiores detalhes da instalação do *device driver*, tal como para outros sistemas operacionais, podem ser obtidas neste [artigo](https://www.robocore.net/tutoriais/instalando-driver-do-nodemcu).

## Instalação do Firmware MicroPython

A instalação do *firmware* MicroPython na placa de desenvolvimento é feita com uso do Thonny.

1. Acesse o site [micropython.org](https://micropython.org/). Acesse a seção "Download" indicada no menu superior.
2. Localize o segmento *Filter by*. Escolha "esp32" ou "esp8266" conforme o modelo da placa de desenvolvimento.
3. Role a página até o final, selecionando o modelo que mais se aproxima da placa (não se preocupe em obter uma correspondência exata).
4. Na nova página exibida, selecione para *download* a versão mais recente disponível (a primeira da lista), que no momento do preparo deste roteiro era: [esp8266-20220618-v1.19.1.bin](https://micropython.org/resources/firmware/esp8266-20220618-v1.19.1.bin).
5. Abra o Thonny.
6. Conecte a placa NodeMCU à porta USB de seu computador.

7. Observe se o console do interpretador Python é iniciado corretamente. Caso contrário: verifique em *Executar | Configurar interpretador* se o interpretador foi selecionado corretamente (MicroPython ESP8266) e se a porta USB para conexão está correta. Acione o botão *OK*. Na janela do editor acione botão *Stop* ou **CTRL+F2** para reiniciar a conexão.
8. Digite o sketch que segue na janela de edição do Thonny. (Não é necessário digitar os comentários, ou seja, as linhas iniciadas por `#`.)

```python
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

```

5. Salve como "00_Hello_World.py".
6. Para executar acione o botão *Executar* ou **F5**.

## Sugestões

* Modifique a mensagem (variável `message`) e execute novamente.
* Imprima várias mensagens diferentes, utilizando outros comandos `print`.

### Simulação

Esta [experiência](https://wokwi.com/projects/345887141617730130) pode ser simulada no [Wokwi](https://wokwi.com/projects/345887141617730130).

---
Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2023-1
