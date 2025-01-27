import hashlib
password = "password145"
hash_object = hashlib.md5(password.encode())
print(hash_object.hexdigest())
