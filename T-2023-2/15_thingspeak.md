# OFC::15 IoT com ThingSpeak 

Nesta montagem continuaremos a explorar a capacidade do NodeMCU ESP8266 de se conectar a redes **Wi-Fi** (*Wireless Fidelity*) para realizar o envio de dados a um serviço na internet: o **ThingSpeak**. 

O **ThingSpeak** (https://thingspeak.com) é uma plataforma de IoT (Internet das Coisas) que permite coletar, analisar e visualizar dados de sensores e de dispositivos conectados. O ThingSpeak permite a criação de *canais* (*channels*) que podem agregar até oito *campos* (*fields*) diferentes, os quais podem armazenar uma série temporal de dados obtidas por um sensor ou outro dispositivo. Tais dados podem ser exibidos em *dashboards* que podem ser consultados na internet por qualquer computador, celular ou outro equipamento; ou ainda recuperados para serem utilizados por outras aplicações.

Uma série temporal de dados é uma sequência de números, inteiros ou reais, associados à um instante específico de tempo, por exemplo, a temperatura de um equipamento, sala ou localidade, registrada a cada 2 minutos, como na figura que segue, que mostra o canal `2287758`, denominado *OCF::random*, acessível pela url https://thingspeak.com/channels/2287758. 
![ThingSpeak Channel](https://github.com/pjandl/ocf/blob/main/T-2023-2/figuras/15_thingspeak_channel.png)

A página de exibição do canal é configurável e pode exibir uma combinação de gráficos e mostradores dos campos agregados pelo canal. Para a criação de um canal, basta abrir uma conta gratuita que, apesar de suas limitações, permite criar alguns canais com vários campos, conveniente para nossa experiência e muitas outras.


## Objetivo

Uso das capacidades de comunicação Wi-Fi do NodeMCU ESP8266 para conexão com uma rede local e acesso à plataforma **ThingSpeak** na internet para envio, consulta e recuperação de dados numéricos aleatórios.

## Lista de Materiais

* Placa NodeMCU ESP8266 (30 pinos)
* Cabo USB-A -- USB-C

## Roteiro

Este roteiro não requer qualquer montagem, visto que serão utilizadas as capacidades embutidas do NodeMCE e a exibição das informações no console do Thonny e no *dashboard* do canal específico do ThingSpeak. 

## Parte I - Envio de dados ao ThingSpeak

Nesta seção veremos como enviar dados do NodeMCU para a plataforma ThingSpeak.

1. Conecte a placa NodeMCU à porta USB de seu computador.
2. Abra o Thonny.
3. Observe se o console do interpretador Python é iniciado corretamente. Caso contrário: verifique em *Executar | Configurar interpretador* se o interpretador foi selecionado corretamente (MicroPython ESP8266) e se a porta de conexão está correta. Acione o botão *Stop* ou **CTRL+F2** para reiniciar a conexão.
4. Digite o sketch que segue.

```python
#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 15_thingspeak_feed.py
# Envio de dados para plataforma de IoT ThingSpeak.
#
from utime import sleep, gmtime
from random import getrandbits
import network
import urequests

# ThingSpeak Write API KEY
TS_WRITE_KEY = 'E9TJXODK7RIJO11C'

# Estabelece modo de funcionamento estação (STA_IF)
estacao = network.WLAN(network.STA_IF)
# Ativa transceiver Wi-Fi
estacao.active(True)
# Conecta da rede ssid com senha
# estacao.connect(ssid, senha)
estacao.connect('j4nd1', 'abc1abc2abc3')
while not estacao.isconnected()\
      and estacao.status() >= 0:
    print('.', end='')
    sleep(1.0)
if not estacao.isconnected():
    raise RuntimeError('Falha na conexão de rede')   
print('\nConexão realizada.\n', estacao.ifconfig())

# url para conexão com ThingSpeak service
url = "https://api.thingspeak.com/update?api_key={}&field1={}"

for t in range(60):
    # gera valor aleatório entre 0 e 1023 (2^10)
    value = getrandbits(10)
    print(t, 20*'-', 'value:', value)
    # envia HTTP get ao ThingSpeak com valor aleatório
    resposta = urequests.get(url.format(TS_WRITE_KEY, value))
    # verifica se resposta OK (código 200)
    if resposta.status_code == 200:
        # determina data-hora atual
        (a,m,d,hh,mm,ss,wd,yd) = gmtime()
        status = "{}/{}/{} {}h{}m{}s".format(a,m,d,hh,mm,ss)
        # obtém e exibe texto da resposta
        texto = resposta.text
        print(type(texto), texto, end=' ')
        # verifica se ocorreu gravação dos dados
        if int(texto) != 0:
            print('Recorded at', status)
        else:
            print('Missed')
    else:
        print('HTML Error:', resposta.status_code)

    print(t, 20*'-')
    # Contas gratuitas não suportam intervalos menores que 1 minuto
    sleep(120.0)
    
estacao.active(False)

```

6. Salve como "15_thingspeak_feed.py".
7. Para executar acione o botão *Executar* ou **F5**.
8. Devem ser exibidas no console do Thonny os dados enviados ao ThingSpeak, incluindo a resposta, que confirma ou não o registro dos dados. O programa efetua o envio 60 vezes, com um intervalo de 2 minutos para cada envio. Modifique se julgar necessário.
9. Carregue a url https://thingspeak.com/channels/2287758 no seu navegador para visualizar o dashboard do canal, observando o recebimento de novos dados a cada 2 minutos.

> :warning: **Aviso:** Para que seja possível o registro de dados, é necessário o envio da *chave da API*, um código numérico que funciona como uma autorização para a gravação de dados. Cada canal possui uma chave própria, que pode ser obtida na configuração do canal na plataforma ThingSpeak. No início deste script, definimos a variável `TS_WRITE_KEY` para conter a chave do canal utilizado.


## Parte II - Recebimento de dados do ThingSpeak

Os dados enviados para o **ThingSpeak** também podem ser recuperados, permitindo que outras aplicações possam utilizá-los para os mais diversos fins.

Nesta seção veremos como recuperar dados da plataforma ThingSpeak com o NodeMCU.

> :bulb: **Dica:** A leitura (recuperação) de dados em canais públicos não requer uma *chave da API* e pode ser feita livremente.

1. Conecte a placa NodeMCU à porta USB de seu computador.
2. Abra o Thonny.
3. Observe se o console do interpretador Python é iniciado corretamente. Caso contrário: verifique em *Executar | Configurar interpretador* se o interpretador foi selecionado corretamente (MicroPython ESP8266) e se a porta de conexão está correta. Acione o botão *Stop* ou **CTRL+F2** para reiniciar a conexão.
4. Digite o sketch que segue.

```python
#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 15_thingspeak_feed.py
# Envio de dados para plataforma de IoT ThingSpeak.
#
from utime import sleep
import network
import urequests

# Estabelece modo de funcionamento estação (STA_IF)
estacao = network.WLAN(network.STA_IF)
# Ativa transceiver Wi-Fi
estacao.active(True)
# Conecta da rede ssid com senha
# estacao.connect(ssid, senha)
estacao.connect('j4nd1', 'abc1abc2abc3')
while not estacao.isconnected()\
      and estacao.status() >= 0:
    print('.', end='')
    sleep(1.0)
if not estacao.isconnected():
    raise RuntimeError('Falha na conexão de rede')   
print('\nConexão realizada.\n', estacao.ifconfig())

# url para conexão com ThingSpeak service
url = "https://api.thingspeak.com/channels/2287758/fields/{}.json?results={}"

print(20*'-')
# envia HTTP get ao ThingSpeak com pedido de 10 dados do canal 1
resposta = urequests.get(url.format(1, 10))
# verifica se resposta OK (código 200)
if resposta.status_code == 200:
    # obtém dados JSON da resposta
    dados = resposta.json()
    # exibe dados do canal
    print(dados['channel']['name'], ':', dados['channel']['id'])
    print(20*'-')
    # exibe leituras obtidas e calcula média
    print('10 last feeds:')
    media = 0
    for r in range(10):
        value = dados['feeds'][r]['field1']
        media += int(value)
        print(value, end=' ')
    media /= 10
    print('\nmedia = ', media)
        
else:
    print('HTML Error:', resposta.status_code)

print(20*'-')    
estacao.active(False)

```

6. Salve como "15_thingspeak_read.py".
7. Para executar acione o botão *Executar* ou **F5**.
8. Devem ser exibidas no console do Thonny as informações obtidas do ThingSpeak em formato JSON (10 últimas leituras do canal), incluindo o cálculo de sua média.

![ThingSpeak Channel](https://github.com/pjandl/ocf/blob/main/T-2023-2/figuras/15_thingspeak_data.png)

---

Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2023-2
