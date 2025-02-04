import hashlib

def hash_md5(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == "__main__":
    password = input("Entrez un mot de passe : ")
    print(f"\t MD5 Hash :")
    print(f"---- {hash_md5(password)}")
