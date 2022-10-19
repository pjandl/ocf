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
