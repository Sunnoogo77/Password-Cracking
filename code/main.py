import hashlib
import itertools


def dictionary_attack(hashed_password, dictionary_file):
    print(f"\nLancement de l'attaque par Dictionaire ====")
    print(f"Hash cible : {hashed_password}")
    with open(dictionary_file, 'r', encoding='latin-1') as f:
        for line in f:
            word = line.strip()
            hash_word = hashlib.md5(word.encode()).hexdigest() 
            if hash_word == hashed_password:
                print(f"\n \t[SUCCESS] Password trouvé: {word}\n")
                return 
    print("\n \tPassword non trouvé \n")

def brute_force_attack(hash_target, chars, max_length):
    print(f"\n \t ---Lancement de l'attaque par Brute Force---")
    print(f"Hash cible : {hash_target} \n")
    
    for length in range(1, max_length + 1):
        print(f"Test des mots de pass de longueur {length}...")
        for guess_tuple in itertools.product(chars, repeat=length):
            guess = ''.join(guess_tuple)
            hash_guess = hashlib.md5(guess.encode()).hexdigest()
            if hash_guess == hash_target:
                print(f"\n \t [SUCCESS] Password trouvé: {guess}\n")
                return
    print("\n[FAILED] Password non trouvé \n")

def genrate_custum_wordlist(output_file, base_words, suffixes=None, prefixes=None):
    
    wordlist = set()
    
    for word in base_words:
        wordlist.add(word)

    if suffixes:
        for word in base_words:
            for suffix in suffixes:
                wordlist.add(word + suffix)
    
    if prefixes:
        for word in base_words:
            for prefix in prefixes:
                wordlist.add(prefix + word)

    with open(output_file, 'w') as f:
        for word in sorted(wordlist):
            f.write(word + "\n")
    print(f"Custum wordlist générée dans : {output_file}")

if __name__ == "__main__":
    print ("=== Password Cracker ===")
    print("1. Dictionary Attack")
    print("2. Brute Force Attack")
    choice = input("\n \t Choix: ")
    
    if choice == "1":
        dictionary_file = input("\nFichier de dictionnaire: ")
        hashed_password = input("Mot de passe hashé: ")
        dictionary_attack(hashed_password, dictionary_file)
    elif choice == "2":
        chars = input("\nCaractères à utiliser: ")
        max_length = int(input("Longueur maximale: "))
        hashed_password = input("Mot de passe hashé: ")
        brute_force_attack(hashed_password, chars, max_length)
    else:
        print("Choix invalide")
    
    
    # dictionary_file = "Input/rockyou.txt"
    # hashed_password = "42c853d6bbd0cfddc2d0978df437fa97"
    
    # target_hash = "512b59c7f685af35221b6cc9b62737c2"
    # chars = "abcdefghijklmnopqrstuvwxyz@!7"
    
    # dictionary_attack(hashed_password, dictionary_file)
    # brute_force_attack(target_hash, chars, 6)  # Longueur max = 6


# import hashlib
# password = "@dm!7"
# hash_object = hashlib.md5(password.encode())
# print("MD5 Hash:", hash_object.hexdigest())

