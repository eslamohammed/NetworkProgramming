///Chat Room

from Socket import *
from _thread import *
import threading

S = Socket (AF_INET , Sock_STREAM)  //Socket function (S) return special number =>file descriptor
host = "127.0.0.1"  //localhost
port = 7000         //8080
S.bind((host , port))           //(()) tuple
S.listen(5)                     //number of requests in queue
Clients = []


def connectNewUser( c , add ):
    while True:
        m = C.recv(2048)
        m = add[0] + ':' + m.encode('utf-8')
        sendToAll( m , C )

def sendToAll( message , Connection):
    for client in Clients:
        if client != Connection:
            client.send(message.encode('utf-8'))

while True:
    c , add = accept()
    Client.append(c)
    Start_new_thread (connectNewUser , ( c . add))