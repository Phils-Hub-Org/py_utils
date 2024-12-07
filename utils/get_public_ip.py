import requests

def getPublicIp() -> str:
    response = requests.get('https://api.ipify.org')
    public_ip = response.text
    return public_ip

if __name__ == '__main__':
    print(getPublicIp())