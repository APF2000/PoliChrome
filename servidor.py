import socket as soc
import sys

host = 'localhost'
port = 51432

# Cria uma porta passiva
s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR,1)

# Associa o socket do servidor a um endereço e começa a ouvir pedidos
# pedidos de conexão
s.bind((host, port))
s.listen()
print("Server is running on port %d; press Ctrl-C to terminate." % port)

# Ao aceitar conexão, recebe e printa a mensagem 
while 1:
    try:
        clientsock, clientaddr = s.accept()
        print ("Got connection from", clientsock.getpeername())
        buf = clientsock.recv(256)
        print("Received : %s" % buf.decode('utf-8'))

    except KeyboardInterrupt:
        raise
        clientsock.close()

    except soc.error as e:
        print("%s : simplex-talk: socket" % e)        
        sys.exit(1)
        
    except Exception as e:
        print( "Error: %s" % e)    
        continue 
    
    clientsock.close()