# OFC::12 Display OLED I2C

Esta montagem mostra a utilização de um display OLED conectado ao NodeMCU ESP8266 por meio do barramento **I2C** para exibição de informações, permitindo que dados númericos e textos sejam apresentados para o usuário, ampliando as possibilidades de utilização de qualquer montagem.

Um *display* é um dispositivo eletrônico utilizado para apresentação de informação de maneira visual, que pode ser embutido em inúmeros equipamentos. Existem [displays](https://pt.wikipedia.org/wiki/Display) de cristal líquido (*Liquid Cristal Display* ou LCD), de LED (*Light-Emiting Diode*) e OLED (*Organic LED*). Um display OLED é composto por uma camada de material orgânico disposta entre dois eletrodos, um deles geralmente transparente. Quando esse material orgânico é estimulado por um campo eletromagnético, ocorre a emissão de luz, sem necessidade do uso da luz de fundo (*backlight*), como nos LCDs. A ausência do *backlight* faz com que esse display seja extremamente econômico em termos de consumo de energia.

Existem displays OLED de diversos tamanho, geralmente suportando a comunicação [I2C](https://pt.wikipedia.org/wiki/I%C2%B2C) (*Inter-Integrated Circuit*) ou [SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface) (*Serial Peripheral Interface*).

O I2C, visto na montagem anterior [OFC::11 Barramento I2C](https://github.com/pjandl/ocf/blob/main/T-2023-2/11_i2c.md), é um protocolo de comunicação serial que permite conectar vários dispositivos de baixa velocidade à um sistema microprocessado. Assim, com uso de apenas duas GPIO, podemos conectar o ESP8266 à um display OLED I2C, além de outros dispositivos no mesmo barramento, simplificando a construção de sistemas integrados ao microcontrolador.

## Objetivo

Uso do barramento I2C para conexão simultânea com múltiplos dispositivos por meio de entradas digitais. Também demonstra a exibição de informação no display OLED I2C.

## Lista de Materiais

* Placa NodeMCU ESP8266 (30 pinos)
* Cabo USB-A -- USB-C
* 01 Display OLED 128x64 I2C
* 01 Protoboard (170 pontos ou mais)
* Jumpers

## Roteiro

Este roteiro requer a montagem simples indicada na figura que segue, onde o barramento de quatro linhas/vias I2C é conectado ao display:
+ **SDA** : *serial data line*, por onde trafegam os dados entre os dispositivos conectados;
+ **SCL** : *serial clock line*, que controla as operações de comunicação;
+ **GND** : *ground*, comum da alimentação; e
+ **VCC** : tensão de alimentação.

![Circuito 12 OLED I2C](https://github.com/pjandl/ocf/blob/main/T-2023-2/figuras/12_oled_i2c.png)

Observe as conexões entre o NodeMCU, o protoboard e o display para constituir o barramento I2C: linha 4 para SDA, linha 5 para SCL, linha 6 para GND e linha 7 para VCC. 

*Preste atenção nas conexões com o display, pois a pinagem **não** é padronizada e varia conforme o fabricante!*

Com esta montagem e o código que segue, é possível exibir informações no display OLED conectado ao NodeMCU pelo barramento I2C.

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
# 12_oled_i2c.py
# Uso de display OLED conectado com protocolo I2C.
#
from machine import Pin, I2C
from time import sleep
import ssd1306

# Configura barramento I2C
i2c = I2C(sda=Pin(4), scl=Pin(5))
# Cria objeto p/ controle do display OLED 128x64 I2C
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

pen = 1 # 1 ativa pontos, 0 desliga pontos
for r in range(4):
    oled.fill(not pen) # preenche display
    oled.rect(0, 0, 128, 16, pen) # retangulo
    oled.text('Ola!', 2, 4, pen) # escreve texto em x,y
    oled.show() # renderiza desenhos e texto
    sleep(3.0)
    oled.text('Tudo bem?', 2, 18, pen)
    oled.show()
    sleep(3.0)
    oled.text('01234567890+-*/', 2, 30, pen)
    oled.text('abcdefghijklmno', 2, 42, pen)
    oled.text('pqstuvxz     =)', 2, 54, pen)
    oled.show()
    sleep(5.0)
    pen = not pen # inverte caneta
    
oled.poweroff() # desliga display

```

6. Salve como "12_oled_i2c.py".
7. Para executar acione o botão *Executar* ou **F5**.
8. Devem ser exibidas várias mensagens, com uma pausa entre elas, alternando a exibição com fundo escuro (pontos apagados) e fundo claro (pontos ligados).

---

Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2023-2
