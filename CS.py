//server
from Socket import *

//function Socket => family , protocol
try S = Socket (AF_INET , Sock_STREAM)  //Socket function (S) return special number =>file descriptor
    S.setsockopt(SOL_SOCKET , SO_REUSEADDR , 1)
    host = "127.0.0.1"  //localhost
    port = 7000         //8080

        S.bind((host , port))           //(()) tuple
        S.listen(5)                     //number of requests in queue
        while True:
            c , add = accept()              ///c is session number like token differ between users "connecters" 
            print("connection done" add[0]) ///add[ ip , portNumber ] -> Socket information of other end 2nd part (client)
                                            /// add[0] zero to get ip only
            x = c.recv(500)                //500 => limit or size
            print("client:", x.decode('utf-8'))         //print message 
            C.send(input("Server:").encode('utf-8'))    //print & insert messageat the same time and send it 
            C.close()                      ///close connection
except error as e:
    print(e)
except KeyboardInterrupt:
    print("Chat is finished")

///client
from Socket import *

S = Socket (AF_NET , Sock_STREAM)  //special number named => file descriptor
host = "127.0.0.1"  //as localhost
port = 7000         //as port 8080
S.connect(( host , port ))
while True:
    S.send(input("Client:").encode('utf-8'))    //print & insert messageat the same time and send it
    y = c.recv(500)                             //500 => limit or size
    print("Server:", y.decode('utf-8'))         //print message  
    C.close()

///problem one client one Server