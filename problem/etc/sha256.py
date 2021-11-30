import hashlib

n = input()
enData = n.encode()
result = hashlib.sha256(enData).hexdigest()
print(result)