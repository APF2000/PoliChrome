import socket, traceback
import sys
import re
import time

if len(sys.argv) < 2:
    print("usage: simplex-talk host")
    sys.exit(1)
    
entrada = sys.argv[1]

tudo = re.split(':|/', entrada)
(host, port) = tudo[0:2]
port = int(port)

archive = tudo[2:]
archive = '/'.join(archive)

ip = socket.gethostbyname(host)

try:
    host = socket.gethostbyaddr(ip)[0]
except socket.herror:
    print("Can't resolve host")
    #sys.exit(-1)
    host = "Unknown host"

while 1:
    # Criando o socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    

    try:
        s.connect((ip, port))
    except socket.error as e:
        print ("%s : simplex-talk: socket error" % e)
        sys.exit(1)
    except socket.gaierror as e:
        print ("%s : simplex-talk: connect error" % e)
        sys.exit(1)     
    except Exception as e:
        print( "Error : %s" % e)    
        continue 

    # Mandando mensagem para o servidor (GET)
    try:        
        data = "GET /%s HTTP/1.1\nHost: %s\n\n" % (archive, host)
        
        data = data.encode('utf-8')

        s.send(data)

    except socket.error as e:
        print ("%s : simplex-talk: socket error" % e)
        sys.exit(1)
    except Exception as e:
        print( "Error: %s" % e)    
        continue

    # Receber o que foi pedido
    try:
        buf = s.recv(256)
        response = buf.decode('utf-8')
        content = response.split('\n')[-1]
    
        print("Received: \n%s" % response)

        s.close()
        break
        
    except Exception as e:
        print( "Error: %s" % e)    
        continue

    s.close()