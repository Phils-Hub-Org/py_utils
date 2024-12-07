import uuid

def generateUuid() -> str:
    return str(uuid.uuid4())

if __name__ == '__main__':
    print(generateUuid())