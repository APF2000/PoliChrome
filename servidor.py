import socket as soc
import sys
import mimetypes
import re

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

    except soc.error as e:
    
        print("%s : simplex-talk: socket" % e)        
        sys.exit(1)

    #except Exception as e:
    #    print( "Error: %s" % e)    
    #    continue 
    
    clientsock.close()