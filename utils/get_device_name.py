import socket

def getDeviceName() -> str:
    device_name = socket.gethostname()
    return device_name

if __name__ == '__main__':
    print(getDeviceName())  # ...