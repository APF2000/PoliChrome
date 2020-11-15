import socket
import sys
import mimetypes
import re
import which_ipv
import threading

import time

import socket, traceback, os, sys
#import * from threading
        

class ClientThread(threading.Thread):

    def __init__(self, socket):

        threading.Thread.__init__(self, target=self.handlechild)
        self.socket = socket
        #print ("New connection added: ", clientAddress)

    def handlechild(clientsock): 

        print("Sou uma nova thread, meu nome e: %s" % threading.currentThread().getName())

        # Bind to all interfaces print "New child", currentThread() .getName() 
        print("Got connection from", clientsock.getpeername())
        while 1: 
            data = clientsock.recv(4096) 
            if not len(data): 
                break 
            
            clientsock.sendall(data) 
            # Close the connection 
            clientsock.close() 
            

    def run(self):

        print("Sou2222 uma nova thread, meu nome e: %s" % threading.currentThread().getName())


        s = self.socket
        #s.listen()

        #import pdb; pdb.set_trace()
        #print("Server is running on port %d; press Ctrl-C to terminate." % self.port)

        # Ao aceitar conexão, recebe e printa a mensagem 
        #while 1:
        print('------------------------------------------------------')
        try:
            #clientsock, clientaddr = s.accept()
            print ("Got connection from", clientsock.getpeername())

            buf = clientsock.recv(256)
            request = buf.decode('utf-8')
            print("Received :\n %s" % request)

            firstline = request.split('\n')[0]
            archive_name = firstline.split(' ')[1]
            archive_name = archive_name[1:]

            print(archive_name)
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

            print("Dormindo por 5 segundos")
            time.sleep(5)

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
    s.listen()

    #import pdb; pdb.set_trace()

    #while True:
        #clientsock, clientAddress = s.accept()
        #newthread = ClientThread(s)

        #import pdb; pdb.set_trace()
        #newthread.start()

        # Set up the socket. 
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        #s.bind((host, port)) 
        #s.listen(1) 
    while 1: 
        try: 
            clientsock, clientaddr = s.accept() 
        except KeyboardInterrupt:

            import pdb; pdb.set_trace()
            raise 
        except Exception as e: 
            #traceback.print_exc() 

            #import pdb; pdb.set_trace()
            continue 

        #import pdb; pdb.set_trace()

        t = ClientThread(socket = s)#target = handlechild, args = [s]) 
        t.setDaemon(1)
        
        t.start()
        t.join() 


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