import hashlib


def dictionary_attack(hashed_password, dictionary):
    with open(dictionary_file, 'r', encoding='latin-1') as f:
        for line in f:
            word = line.strip()
            hash_word = hashlib.md5(word.encode()).hexdigest() 
            if hash_word == hashed_password:
                print(f"Password trouvé: {word}")
                return 
    print("Password non trouvé")

def brute_force_attack(hashed_password, chars, max_length):
    for length in range(1, max_length + 1):
        for word in itertools.product(chars, repeat=length):
            word = ''.join(word)
            hash_word = hashlib.md5(word.encode()).hexdigest()
            if hash_word == hashed_password:
                print(f"Password trouvé: {word}")
                return
    print("Password non trouvé")

    
if __name__ == "__main__":
    # print ("=== Password Cracker ===")
    # print("1. Dictionary Attack")
    # print("2. Brute Force Attack")
    # choice = input("Choix: ")
    
    # if choice == "1":
    #     dictionary_file = input("Fichier de dictionnaire: ")
    #     hashed_password = input("Mot de passe hashé: ")
    #     dictionary_attack(hashed_password, dictionary_file)
    # elif choice == "2":
    #     chars = input("Caractères à utiliser: ")
    #     max_length = int(input("Longueur maximale: "))
    #     hashed_password = input("Mot de passe hashé: ")
    #     brute_force_attack(hashed_password, chars, max_length)
    # else:
    #     print("Choix invalide")
    
    
    dictionary_file = "Input/rockyou.txt"
    hashed_password = "5f4dcc3b5aa765d61d8327deb882cf99"
    dictionary_attack(hashed_password, dictionary_file)
    brute_force_attack(hashed_password, "abcdefghijklmnopqrstuvwxyz", 5)

