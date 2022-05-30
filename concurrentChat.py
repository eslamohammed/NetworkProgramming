//server
from Socket import *
from _thread import *
import threading

def receive_thread (C):
    while True:
        X = C.recv(200)
        print("client:", x.decode('utf-8'))         //print message

def client_thread(C):
    receive = threading.Thread(traget = receive_thread , arg = (c,))
    receive.Start()
    receive.Join()
    while True:
        C.send(input("Server:").encode('utf-8'))    //print & insert messageat the same time and send it

//function Socket => family , protocol
try S = Socket (AF_INET , Sock_STREAM)  //Socket function (S) return special number =>file descriptor
    S.setsockopt(SOL_SOCKET , SO_REUSEADDR , 1)
    host = "127.0.0.1"  //localhost
    port = 7000         //8080
        S.bind((host , port))           //(()) tuple
        S.listen(5)                     //number of requests in queue
        while True:
            c , add = accept()               ///c is session number like token differ between users "connecters" 
            print("connection done" add[0])  ///add[ ip , portNumber ] -> Socket information of other end 2nd part (client)
                                             /// add[0] zero to get ip only
            Start_new_thread(client_thread , (C,))
except error as e:
    print(e)
except KeyboardInterrupt:
    print("Chat is finished")

///client
from Socket import *
from _thread import *
import threading

def receive_thread(S):
    while True:
    x = C.recv(500)
    print("client:", x.decode('utf-8'))         //print message

S = Socket (AF_NET , Sock_STREAM)  //special number named => file descriptor
host = "127.0.0.1"  //as localhost
port = 7000         //as port 8080
S.connect(( host , port ))
receive = threading.Thread(traget = receive_thread , arg = (S,))
receive.Start()
while True:
    S.send(input("Client:").encode('utf-8'))    //print & insert messageat the same time and send it
    