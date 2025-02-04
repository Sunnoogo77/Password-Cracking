import hashlib

def hash_sha1(password: str) -> str:
    return hashlib.sha1(password.encode()).hexdigest()

if __name__ == "__main__":
    password = input("Entrez un mot de passe : ")
    print(f"\t SHA1 Hash : ")
    print(f"----------- {hash_sha1(password)}")
