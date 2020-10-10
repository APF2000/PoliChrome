import socket, traceback
import sys


if len(sys.argv) < 2:
    print("usage: simplex-talk host")
    sys.exit(1)
    
host = sys.argv[1]
port = 51432

#print("oi")
tudo = socket.gethostbyaddr(host)
host = tudo[0]
ip = tudo[2][0]

#print(ip, host)
#print("oi2")

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

    # Mandando mensagem para o servidor
    try :
        #data = input("Send data to server:\n").encode('utf-8')
        archive = input("Nome do arquivo?\n")
        data = "GET /%s HTTP/1.1\nHost: %s\n\n" % (archive, host)
        data = data.encode('utf-8')

        s.send(data)

    except socket.error as e:
        print ("%s : simplex-talk: socket error" % e)
        sys.exit(1)
    except Exception as e:
        print( "Error: %s" % e)    
        continue
    
        #serversock, serveraddr = s.accept()
        #print ("Got connection from", serversock.getpeername())
    
    try:
        buf = s.recv(256)
        response = buf.decode('utf-8')
        content = response.split('\n')[-1]
    
        print("Received2: %s" % content)
    except Exception as e:
        print( "Error: %s" % e)    
        continue

    s.close()
  
  
  
  
  
  
  
  
# Driver code 