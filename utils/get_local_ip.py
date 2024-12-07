import socket

def getLocalIp() -> str:
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

if __name__ == '__main__':
    print(getLocalIp())