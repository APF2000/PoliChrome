import socket

# Da preferencia ao IPv6
def ipv_qual(host, port):
    #import pdb; pdb.set_trace()

    # IPv4 ou IPv6?
    results = socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM)

    #import pdb; pdb.set_trace()

    ipv_qual = None

    # Verifica para cada resultado retornado
    for result in results:
        # Dizer se e IPv4 ou IPv6

        if result[0] == socket.AF_INET6:
            print("Family: AF_INET6")
            return socket.AF_INET6
        elif result[0] == socket.AF_INET:
            print("Family: AF_INET")
            ipv_qual = socket.AF_INET
        else:
            # Nao e nem um nem outro
            print("Family:", result[0])

    return ipv_qual