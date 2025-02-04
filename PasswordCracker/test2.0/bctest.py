import bcrypt

hashed = bcrypt.hashpw("com".encode(), bcrypt.gensalt())
print(hashed)
