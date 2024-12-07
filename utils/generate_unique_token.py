import uuid, time, secrets

def generateUniqueToken():
    """
    Generates a unique token using UUID and secure random bytes.
    
    Returns:
        str: A unique token with very low chances of duplication.
    """
    # Generate a random UUID
    random_uuid = uuid.uuid4()
    
    # Generate secure random bytes
    secure_random_bytes = secrets.token_hex(8)  # 16 hex characters (8 bytes)

    # Combine UUID and secure random bytes, using the current timestamp
    timestamp = int(time.time() * 1000)  # Milliseconds since epoch
    unique_token = f"{random_uuid}-{secure_random_bytes}-{timestamp}"
    
    return unique_token

if __name__ == '__main__':
    print(generateUniqueToken())  # 31e432a4-a764-46bc-9ea2-12b14c62501c-20567f1559444d48-1730458633341