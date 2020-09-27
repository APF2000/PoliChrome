import socket, traceback
import sys

if len(sys.argv) < 2:
    print("usage: simplex-talk host")
    sys.exit(1)
    
host = sys.argv[1]
port = 51432

while 1:
    # Criando o socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    

    try:
        s.connect((host, port))
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
        data = input("Send data to server:\n").encode('utf-8')
        s.send(data)
    except socket.error as e:
        print ("%s : simplex-talk: socket error" % e)
        sys.exit(1)
    except Exception as e:
        print( "Error: %s" % e)    
        continue 

    s.close()
