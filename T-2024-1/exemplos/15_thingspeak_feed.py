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
