import hashlib as Hash

def hash(rawUserInput):
    blake2B = Hash.blake2b()
    blake2B.update(rawUserInput.encode())
    
    return blake2B.hexdigest()