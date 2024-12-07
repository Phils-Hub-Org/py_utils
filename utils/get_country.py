import requests

def getCountry() -> str:
    response = requests.get('https://ipinfo.io')
    data = response.json()
    return data['country']

if __name__ == '__main__':
    print(getCountry())