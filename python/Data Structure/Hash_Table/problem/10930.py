import hashlib

def hash(data):
    result = hashlib.sha256(data.encode())
    print(result.hexdigest())

data = input()
hash(data)