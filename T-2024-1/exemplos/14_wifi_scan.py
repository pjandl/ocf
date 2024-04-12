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

# Exibe redes descobertas
print("{:30s}|{:5s}|{:5s}".format("SSID Rede", "Canal", "Sinal"))
print(30*'-', 5*'-', 5*'-')
for r in redes:
    print("{:30s}|{:5d}|{:5d}".format(r[0], r[2], r[3]))

# Desativa transceiver Wi-Fi
estacao.active(True)
