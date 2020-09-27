import socket, traceback
import sys

if len(sys.argv) < 3:
    print("Too few arguments")
    sys.exit(-1)
    
host = sys.argv[1]
port = int(sys.argv[2])


    
while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.error as e:
        print ("Strange error creating socket: %s" % e)
        sys.exit(1)
    except socket.gaierror as e:
        print ("Error connecting to server: %s" % e)
        sys.exit(1)
    #import pdb; pdb.set_trace()
    import time


    #buf = s.sendmsg([b'Redes e chato'])
    
    #if not len(buf):
    #    break
    #sys.stdout.write(buf)
    
    try:
        #s.connect((host, port))
        #s.sendall(buf.encode('utf-8'))
        time.sleep(2)
        s.send(b"Teste 123")

    except socket.error as e:
        print ("Strange error creating socket: %s" % e)
        sys.exit(1)
