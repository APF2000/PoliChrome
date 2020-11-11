import socket
import sys
import mimetypes
import re
import which_ipv
import threading

def thread_function():
    print('Thread function')

class ClientThread(threading.Thread):

    def _init_(self, socket, port):

        import pdb; pdb.set_trace()

        threading.Thread.__init__(self, target = thread_function)
        self.socket = socket
        self.port = port
        print ("New connection added: %s" % "eae mano")

    def run(self):

        s.listen()
        print("Server is running on port %d; press Ctrl-C to terminate." % self.port)

        # Ao aceitar conexão, recebe e printa a mensagem 
        while 1:
            print('------------------------------------------------------')
            try:
                clientsock, clientaddr = s.accept()
                print ("Got connection from", clientsock.getpeername())

                buf = clientsock.recv(256)
                request = buf.decode('utf-8')
                print("Received :\n %s" % request)

                firstline = request.split('\n')[0]
                archive_name = firstline.split(' ')[1]
                archive_name = archive_name[1:]

                print(archive_name)

                #import pdb; pdb.set_trace()
                try:
                    archive = open(archive_name, 'r').read()

                    status = "HTTP/1.1 200 OK\n"
                    length = "Content-Length: %d\n" % len(archive)
                    content = "Content-Type: %s\n\n" % mimetypes.MimeTypes().guess_type(archive_name)[0]
                
                    data = status + length + content + archive
                except FileNotFoundError:
                    print("%s not found\n" % archive_name)
                    data = "HTTP/1.1 400 ERRO \n\n"
                    #continue      
                    
                data = data.encode('utf-8')

                clientsock.sendall(data)
                clientsock.close()

            except KeyboardInterrupt:
                raise
                clientsock.close()

            except socket.error as e:
            
                print("%s : simplex-talk: socket" % e)        
                sys.exit(1)

            #except Exception as e:
            #    print( "Error: %s" % e)    
            #    continue 
            
            clientsock.close()

if __name__ == '__main__':

    host = 'localhost'
    port = 51432

    ipv_qual = which_ipv.ipv_qual(host, port)

    # Cria uma porta passiva
    s = socket.socket(ipv_qual, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    # Associa o socket do servidor a um endereço e começa a ouvir pedidos
    # pedidos de conexão
    s.bind((host, port))

    while True:
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()


""" 
class ClientThread(threading.Thread):
    def _init_(self,clientAddress,clientsocket):
        threading.Thread._init_(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        print ("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg=='bye':
              break
            print ("from client", msg)
            self.csocket.send(bytes(msg,'UTF-8'))
        print ("Client at ", clientAddress , " disconnected...")
LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start() """