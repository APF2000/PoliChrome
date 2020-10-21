import socket, traceback
import sys
import re
import time
#import ipadress

import which_ipv

MAX_BUFFER = 1024 #256

# ip:porta/arquivo ou nome:porta/arquivo.

if len(sys.argv) < 2:
    print("usage: simplex-talk host")
    sys.exit(1)
    
entrada = sys.argv[1]

tudo = re.split(':|/', entrada)
(host, port) = tudo[0:2]
port = int(port)

archive = tudo[2:]
archive = '/'.join(archive)

#import pdb; pdb.set_trace()

# Criando o socket (consegue pedir IPv4 ou IPv6)
ipv_qual = which_ipv.ipv_qual(host, port)
s = socket.socket(ipv_qual, socket.SOCK_STREAM)

#ip = socket.gethostbyname(host)
ip = socket.getaddrinfo(host, None, ipv_qual)[0][4][0] # nao pergunte por que
print(ip)

#print("Batata")
#print(socket.getfqdn(ip))

try:
    #host = socket.gethostbyaddr(ip)[0]
    print(host)
except socket.herror:
    print("Can't resolve host")
    #sys.exit(-1)
    host = "Unknown host"

while 1:
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
        #import pdb; pdb.set_trace()

        data = "GET /%s HTTP/1.1\r\nHOST: %s\r\n\r\n" % (archive, host)
        
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
        buf = s.recv(MAX_BUFFER)
        response = buf.decode('utf-8')
        content = response.split('\n')[-1]
    
        print("Received: \n%s" % response)

        s.close()
        break
        
    except Exception as e:
        print( "Error: %s" % e)    
        continue

    s.close()