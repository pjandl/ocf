# OFC::14 Wi-Fi 

Nesta montagem vamos explorar a capacidade do NodeMCU ESP8266 de se conectar a redes **Wi-Fi** (*Wireless Fidelity*), uma tecnologia que permite a conexão sem fio de dispositivos, o que possibilita sua interligação em rede e o acesso à internet. 

O NodeMCU ESP8266 oferece suporte para conexões Wi-Fi nos padrões IEEE 802.11 b/g/n, com velocidade de até 150 Mbps. É capaz de funcionar nos modos
STA (*station*), AP (*access point*) e STA+AP (*station* e *access point* simultaneamente). Devido sua antena externa, possui boa sensibilidade, o que se traduz em alcance bastante satisfatório.

Com uso de módulos específicos, o ESP8266 é capaz de se conectar à redes de computadores com uso de diferentes protocolos, tais como HTTP, TCP/IP, MQTT e FTP, possibilitando incontáveis aplicações.

## Objetivo

Uso das capacidades de comunicação Wi-Fi do NodeMCU ESP8266 para conexão com uma rede local e acesso ao serviço **WorldTime** da internet para obtenção de data e hora.

## Lista de Materiais

* Placa NodeMCU ESP8266 (30 pinos)
* Cabo USB-A -- micro-USB

## Roteiro

Este roteiro não requer qualquer montagem, visto que serão utilizadas as capacidades embutidas do NodeMCE e a exibição das informações obtidas no console do Thonny. 

## Parte I - Descoberta de redes Wi-Fi

Nesta seção veremos como descobrir as redes Wi-Fi disponíveis no local onde está o NodeMCU.

1. Conecte a placa NodeMCU à porta USB de seu computador.
2. Abra o Thonny.
3. Observe se o console do interpretador Python é iniciado corretamente. Caso contrário: verifique em *Executar | Configurar interpretador* se o interpretador foi selecionado corretamente (MicroPython ESP8266) e se a porta de conexão está correta. Acione o botão *Stop* ou **CTRL+F2** para reiniciar a conexão.
4. Digite o sketch que segue.

```python
#
# Oficina de Computação Física
# Prof. Peter Jandl Jr
#
# 14_wifi.py
# Descoberta de redes Wi-Fi disponíveis no local do NodeMCU.
#
import network

# Estabelece modo de funcionamento estação (STA_IF)
estacao = network.WLAN(network.STA_IF)

# Ativa transceiver Wi-Fi
estacao.active(True)

# Efetua varredura para descoberta das redes
redes = estacao.scan()

# Exibe redes descobertas sem formatação
# print(redes)

# Exibe redes descobertas como uma tabela
print("{:30s}|{:5s}|{:5s}".format("SSID Rede", "Canal", "Sinal"))
print(30*'-', 5*'-', 5*'-')
for r in redes:
    print("{:30s}|{:5d}|{:5d}".format(r[0], r[2], r[3]))

# Desativa transceiver Wi-Fi
estacao.active(True)

```

6. Salve como "14_wifi_scan.py".
7. Para executar acione o botão *Executar* ou **F5**.
8. Devem ser exibidas no console do Thonny as redes Wi-Fi no alcance do NodeMCU, como na figura que segue.
![Wi-Fi Scan](https://github.com/pjandl/ocf/blob/main/T-2023-2/figuras/14_wifi_scan.png)

> :warning: **Aviso:** Ao finalizar os *scripts* ou quando os intervalos de transmissão forem muito grandes, desative o transceiver Wi-Fi para reduzir o consumo de energia no dispositivo.

> :bulb: **Dica:** Você pode simplificar este *script* descomentando `print(redes)` e comentando o trecho seguinte, que mostra as redes como uma tabela.


## Parte II - Acesso ao *WorldTime Service*

O **WorldTime Service** é um serviço na internet que fornece informações sobre datas, horários e fusos horários em todo o mundo, que pode ser acessado gratuitamente para atualizar o horário de relógios, computadores e outros dispositivos, como placas NodeMCU.

Nesta seção veremos como o NodeMCU pode ser conectar a uma rede Wi-Fi e, via internet, acessar o WorldTime Service para obter a data e horário atuais.

1. Conecte a placa NodeMCU à porta USB de seu computador.
2. Abra o Thonny.
3. Observe se o console do interpretador Python é iniciado corretamente. Caso contrário: verifique em *Executar | Configurar interpretador* se o interpretador foi selecionado corretamente (MicroPython ESP8266) e se a porta de conexão está correta. Acione o botão *Stop* ou **CTRL+F2** para reiniciar a conexão.
4. Digite o sketch que segue.

```python
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
estacao.connect(ssid, senha)
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

```

6. Salve como "14_worldtime.py".
7. Para executar acione o botão *Executar* ou **F5**.
8. Devem ser exibidas no console do Thonny as informações obtidas do WorldTime Service em formato JSON e, ao final, a data e hora obtidas do serviço e em vigor no NodeMCU.
9. Se desejado, descomente o trecho de código que possibilita a atualização do *Real Time Clock* (RTC) interno do NodeMCU.

---

Oficina de Computação Física | Prof. Peter Jandl Jr
<br/>2023-2
