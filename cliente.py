import socket, traceback
import sys
import re
import time
import which_ipv

# Para rodar o cliente
# ip:porta/arquivo ou nome:porta/arquivo
# ex: python3 cliente.py localhost:51423/

MAX_BUFFER = 1024 #256

if len(sys.argv) < 2:
    print("usage: simplex-talk host")
    sys.exit(1)
    
entrada = sys.argv[1]

# Pegar ipv4, ipv6 e nome de dominio
# XXX.XXX.XXX.XXX:YY/slaoq
# XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:YY/slaoq
# www.blabla.com.gov.enois.br:80/slaoq
# ex: 2800:3f0:4001:81c::2004:80/

tudo = entrada.split('/')
archive = '/'.join(tudo[1:])
hostport = tudo[0].split(':')
port = int(hostport[-1])
host = ':'.join(hostport[:-1])


# Criando o socket (consegue pedir IPv4 ou IPv6)
ipv_qual = which_ipv.ipv_qual(host, port)
s = socket.socket(ipv_qual, socket.SOCK_STREAM)

#ip = socket.gethostbyname(host)
ip = socket.getaddrinfo(host, None, ipv_qual)[0][4][0] # nao pergunte por que
print(ip)

try:
    # Descomentar so pro localhost (que e o que da certo)
    #host = socket.gethostbyaddr(ip)[0]
    print(host)
except socket.herror:
    print("Can't resolve host")
    #sys.exit(-1)
    host = "Unknown host"

while 1:
    try:
        #import pdb; pdb.set_trace()
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
        data = "GET /%s HTTP/1.1" % archive
        if host != ip:
            data += "\r\nHOST: %s" % host
        data += "\r\n\r\n"

        print(data)
        
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