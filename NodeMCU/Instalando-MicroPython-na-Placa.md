# Instalando o MicroPython nas Placas de Desenvolvimento

Nos roteiros desenvolvidos nesta oficina, escolhemos o Python como linguagem de programação para controlarmos as placas de desenvolvimento utilizadas nos protótipos construídos. Esta linguagem foi escolhida por três razões: sua simplicidade permite uma aprendizagem mais rápida; é uma das preferidas tanto no âmbito acadêmico, como no mercado comercial de programação; possui uma enorme biblioteca de módulos que agilizam o desenvolvimento de soluções.

MicroPython é uma implementação de software muito compatível com a linguagem de programação Python 3, escrita em C e otimizada para ser executadas em um microcontrolador. É composta de um compilador Python para bytecode e um interpretador desse bytecode capaz de executar programas escritos em Python em placas de desenvolvimento específicas.

## Objetivo

Efetuar a instalação do *firmware* MicroPython em uma placa de desenvolvimento, possibilitando sua utilização na prototipagem de soluções de computação física (e também internet das coisas).

## Lista de Materiais

* Placa NodeMCU ESP8266 ou ESP32
* Cabo USB-A -- micro-USB

## Roteiro

Este roteiro não requer qualquer montagem, apenas a conexão da placa NodeMCU ao computador, possibilitando a instalação do *firmware* MicroPython na placa de desenvolvimento com uso do IDE Thonny.

## Instalação do Thonny

O IDE Thonny é um ambiente de desenvolvimento integrado para Python, que integra um editor de programas, um console para execução dos programas e um depurador; o que torna o trabalho de programar mais simples. Além disso, permite a conexão com várias placas de desenvolvimento, além de executar a instalação do *firmware* MicroPython nestas placas.

1. Faça o *download* do IDE Thonny em [https://thonny.org/](https://thonny.org/). Selecione a versão adequada ao seu sistema operacional. A versão *Installer with 64-bit Python 3.X* (onde X pode ser 10, 11, ...) é bastante conveniente.
2. Execute o instalador, aceite a licensa e escolha as opções de instalação que julgar adequadas em relação ao diretório de instalação, idioma e criação de atalhos.
3. Execute o Thonny.
![IDE Thonny](https://github.com/pjandl/ocf/blob/main/NodeMCU/figuras/thonny_ide_1.png)
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
![Execução de programa no IDE Thonny](https://github.com/pjandl/ocf/blob/main/NodeMCU/figuras/thonny_ide_2.png)

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
2. Localize o segmento *Filter by*. Escolha "esp32" ou "esp8266" conforme o modelo da placa de desenvolvimento. Você deve localizar a página [https://micropython.org/download/?port=esp8266](https://micropython.org/download/?port=esp8266).
3. Role a página até o final, selecionando o modelo que mais se aproxima da placa (não se preocupe em obter uma correspondência exata).
4. Na nova página exibida, selecione para *download* a versão mais recente do *firmware* disponível (a primeira da lista), que no momento do preparo deste roteiro era: [ESP8266_GENERIC-20240222-v1.22.2.bin](https://micropython.org/resources/firmware/ESP8266_GENERIC-20240222-v1.22.2.bin).
5. Abra o Thonny.
6. Conecte a placa NodeMCU à porta USB de seu computador.
7. Acione a opção *Executar | Configurar interpretador*. Selecione o interpretador correto (MicroPython ESP8266) e verifique se a porta USB para conexão está correta (ou mantenha a opção *Tente detectar a porta automaticamente*). Na parte inferior da janela, acione o link *Instalar ou atualizar MicroPython*.
![Execução de programa no IDE Thonny](https://github.com/pjandl/ocf/blob/main/NodeMCU/figuras/thonny_ide_3.png)
8. Na janela que surge, selecione a porta USB para conexão (ou use a opção *Tente detectar a porta automaticamente*) e localize o arquivo correspondente ao *firmware* desejado (*download* do item 4). Em *Flash mode* selecione *From iamge file (keep)* e marque *Erase flash before installing*.
![Execução de programa no IDE Thonny](https://github.com/pjandl/ocf/blob/main/NodeMCU/figuras/thonny_ide_4.png)
9. Acione **Instalar** e aguarde.
![Execução de programa no IDE Thonny](https://github.com/pjandl/ocf/blob/main/NodeMCU/figuras/thonny_ide_5.png)
Quando a gravação do *firmware* for concluída, acione **Fechar**.
10. Verifique no *Shell* (console do Python) a conexão com a placa ESP8266 e a versão instalada.
![Execução de programa no IDE Thonny](https://github.com/pjandl/ocf/blob/main/NodeMCU/figuras/thonny_ide_6.png)


## Sugestões

* Modifique a mensagem (variável `message`) e execute novamente.
* Imprima várias mensagens diferentes, utilizando outros comandos `print`.

### Simulação

Esta [experiência](https://wokwi.com/projects/345887141617730130) pode ser simulada no [Wokwi](https://wokwi.com/projects/345887141617730130).

---
Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2024-1
