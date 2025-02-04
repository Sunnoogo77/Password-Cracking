import bcrypt

def hash_bcrypt(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

if __name__ == "__main__":
    password = input("Entrez un mot de passe : ")
    print(f"\n \t Bcrypt Hash : ")
    print(f"----------- {hash_bcrypt(password)}")
