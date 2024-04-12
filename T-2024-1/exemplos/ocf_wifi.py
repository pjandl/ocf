import network
import usocket as socket
import utime
import gc
gc.collect()

def define_estacao(ssid, senha, time_out=2**18):
    estacao = network.WLAN(network.STA_IF)
    estacao.active(True)
    estacao.connect(ssid, senha)
    while not estacao.isconnected()\
          and estacao.status() >= 0\
          and time_out > 0:
        print('.', end='')
        utime.sleep(1)
        time_out -= 1
    if not estacao.isconnected():
        raise RuntimeError('Falha na conexão de rede')   
    print('\nConexão realizada.\n', estacao.ifconfig())
    return estacao

def cria_soquete(porta=0, max_req=0):
    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if porta != 0: soquete.bind(('', porta))
    if max_req != 0: soquete.listen(max_req)
    return soquete
    
def cabecalho_http(conexao):
    conexao.send('HTTP/1.1 200 OK\n')
    conexao.send('Content-Type: text/html\n')
    conexao.send('Connection: close\n\n')

def obter_arquivo(arquivo):
    conteudo = ''
    a = open(arquivo, 'rb')
    conteudo = a.read()
    a.close()
    return conteudo
