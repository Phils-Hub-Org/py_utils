import socket

def hasInternet():
    try:
        # Connect to an external DNS server (e.g., Google)
        # You can replace the IP with another reliable server if needed
        socket.create_connection(('8.8.8.8', 53), timeout=5)
        return True
    except OSError:
        return False

# Example usage
if __name__ == '__main__':
    if hasInternet():
        print('Internet is available')
    else:
        print('No internet connection')
