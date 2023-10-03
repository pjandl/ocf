#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 14_worldtime.py
# Acesso ao serviço de data e hora mundial
# WorldTime na internet.
#
from machine import RTC, Pin
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

# NodeMCU real time clock
rtc = RTC()

# conexão com WorldTime Service
url = "http://worldtimeapi.org/api/timezone/America/Sao_Paulo"
resposta = urequests.get(url)
if resposta.status_code == 200:
    print("JSON:", resposta.text)
    json = resposta.json()
    agora = str(json["datetime"])
    ano = int(agora[0:4])
    mes = int(agora[5:7])
    dia = int(agora[8:10])
    hh = int(agora[11:13])
    mm = int(agora[14:16])
    ss = int(agora[17:19])
    us = int(round(int(agora[20:26]) / 10000))
    print('Data WTS: {:02d}/{:02d}/{:04d} {:02d}h{:02d}m{:02d}s'\
          .format(dia, mes, ano, hh, mm, us))
    # Atualiza o RTC do NodeMCU
    # rtc.datetime((ano, mes, dia, 0, hh, mm, ss, us))
    # print('RTC atualizado.')
    
data = "{2:02d}/{1:02d}/{0:4d}".format(*rtc.datetime())
hora = "{4:02d}h{5:02d}m{6:02d}s".format(*rtc.datetime())
print ('Data MCU:', data, hora)

# Desativa transceiver Wi-Fi
estacao.active(False)
