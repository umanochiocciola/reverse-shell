import socket
import sys

def ricevi_comandi(conn):
    stuff = conn.recv(4096).decode()
    print(str(stuff.replace('\r\n', '\n')))
    
    data = input('$ ')
    try:
        conn.sendall(data.encode())
    except: print('connection terminated')

def sub_server(indirizzo, backlog=1):
    print("server started")
    while 1:
        try:
            s = socket.socket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(indirizzo)                     
            s.listen(backlog)                     
            print('Ready to accept a new connection')
            conn, indirizzo_client = s.accept()
            ricevi_comandi(conn)
        except socket.error as error:
            print(f"Something went wrong\n{error}")
        


sub_server(("", 5400))
