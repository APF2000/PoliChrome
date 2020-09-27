import socket as soc
import sys

host = 'localhost'
port = 51423

s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR,1)

s.bind((host, port))
s.listen()

print("Server is running on port %d; press Ctrl-C to terminate." % port)
while 1:
    try:
        clientsock, clientaddr = s.accept()
        print ("Got connection from", clientsock.getpeername())
        buf = clientsock.recv(2048)
        print("Received : %s" % str(buf))
        #import pdb; pdb.set_trace()

    except KeyboardInterrupt:
        raise
        clientsock.close()

    except soc.error as e:
        print( "Error receiving data: %s" % e)        
        sys.exit(1)
        
    except Exception as e:
        #import pdb; pdb.set_trace()
        print( "Error: %s" % e)      
        #traceback.print_exc()
        continue 
    
    clientsock.close()
