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
