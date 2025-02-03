import itertools
from RuleApplyer import *
from urllib.request import urlopen, hashlib
import hashlib
import bcrypt
from concurrent.futures import ThreadPoolExecutor

# Function to read file content and return as list of lines
def getFileInfo(filePath: str):
    try:
        with open(filePath, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"❌ Erreur : Fichier {filePath} introuvable.")
        return []

class passwordCracker:
    NO_HASH = 0
    SHA1 = 1
    MD5 = 2
    BCRYPT = 3
    
    def __init__(self, inputPasswordFile: str, oFile: str):
        self.passwordList = getFileInfo(inputPasswordFile)
        self.outputFile = open(oFile, "w+", encoding="utf-8")
        self.hashNumber = passwordCracker.NO_HASH
        self.verbose = False
        self.appendMask = []
        self.prependMask = []
        self.ruleList = []
        self.numCracked = 0
        self.bcrypt_hashes = []
        self.load_bcrypt_hashes(inputPasswordFile)
        self.stop_attack = False

    # Setters for various configurations
    def setHashNum(self, num: int):
        self.hashNumber = num
    
    def setVerboseMode(self, verboseMode: bool):
        self.verbose = verboseMode

    def setAppendMask(self, am: str):
        self.appendMask = am
    
    def setPrependMask(self, pm: str):
        self.prependMask = pm
    
    def setRuleList(self, rl: list):
        self.ruleList = rl
        
    def loadKeyspaceFromFile(filePath :str) -> str:
        try:
            with open(filePath, 'r', encoding='utf-8') as file:
                keyspace = ''.join(line.strip() for line in file if line.strip())
            return keyspace
        except FileNotFoundError:
            print(f"❌ Fichier {filePath} introuvable.")
            return ""

    # Function to get hash of a password based on the selected hash type
    def getHash(self, password: str):
        if self.verbose:
            print(f"Trying to crack password: {password}")
        if self.hashNumber == passwordCracker.SHA1:
            return hashlib.sha1(password.encode('utf-8')).hexdigest()
        elif self.hashNumber == passwordCracker.MD5:
            return hashlib.md5(password.encode('utf-8')).hexdigest()
        return password
    
    def load_bcrypt_hashes(self, inputPasswordFile):
        try:
            with open(inputPasswordFile, 'r') as f:
                for line in f:
                    hash_str = line.strip()
                    try:
                        bcrypt_hash = hash_str.encode('latin-1')
                        self.bcrypt_hashes.append(bcrypt_hash)
                    except UnicodeEncodeError:
                        print(f"Erreur d'encodage pour le hash : {hash_str}")
        except FileNotFoundError:
            print(f"❌ Erreur : Fichier {inputPasswordFile} INTROUVABLE.")
    
    # Function to compare passwords based on the selected hash type
    # def comparePasswords(self, plainTextPassword: str, hashed_password: bytes | str) -> bool:
    #     if self.hashNumber != passwordCracker.BCRYPT:
    #         possible_hash =  self.getHash(plainTextPassword)
    #         return possible_hash == hashed_password
    #     else :
    #         try:
    #             encoded_password = plainTextPassword.encode('utf-8')
    #             return bcrypt.checkpw(encoded_password, hashed_password)
    #         except (ValueError, TypeError) as e:
    #             print(f"⚠️ Erreur : Impossible de vérifier le mot de passe BCRYPT : {e}")
    #             return False
    def comparePasswords(self, possiblePassword: str, hashed_password: bytes | str) -> bool:
        if self.hashNumber == passwordCracker.BCRYPT:
            try:
                encoded_password = possiblePassword.encode('utf-8')
                return bcrypt.checkpw(encoded_password, hashed_password)
            except (ValueError, TypeError) as e:
                print(f"⚠️ Erreur : Impossible de vérifier le mot de passe BCRYPT : {e}")
                return False
        elif isinstance(hashed_password, str):
            return possiblePassword == hashed_password  # ✅ Correction ici
        else:
            return False


            
    
    
    
    # Function to check if a plain text password matches any hashed password in the list
    # def passwordCheck(self, plainTextPassword):
    #     if self.hashNumber == passwordCracker.BCRYPT:
    #         for bcrypt_hash in list(self.bcrypt_hashes):
    #             if self.comparePasswords(plainTextPassword, bcrypt_hash):
    #                 print(f"✅ Mot de passe trouvé : {plainTextPassword}")
    #                 self.numCracked += 1
    #                 self.outputFile.write(plainTextPassword + "\n")
    #                 self.outputFile.flush()
    #                 self.bcrypt_hashes.remove(bcrypt_hash)
                    
    #                 if not self.bcrypt_hashes:
    #                     return True
    #         return False
        
    #     else:
    #         possiblePassword = self.getHash(plainTextPassword)
    #         for password in list(self.passwordList):
    #             if self.comparePasswords(possiblePassword, password):
    #                 print(f"✅ Mot de passe trouvé : {plainTextPassword}")
    #                 self.numCracked += 1
    #                 self.outputFile.write(plainTextPassword + "\n")
    #                 self.outputFile.flush()
    #                 self.passwordList.remove(password)
                    
    #             if len(self.passwordList) == 0:
    #                 return True
    #         return False
    def passwordCheck(self, plainTextPassword):
        if self.hashNumber == passwordCracker.BCRYPT:
            for bcrypt_hash in list(self.bcrypt_hashes):
                if self.comparePasswords(plainTextPassword, bcrypt_hash):
                    print(f"✅ Mot de passe trouvé : {plainTextPassword}")
                    self.numCracked += 1
                    self.outputFile.write(plainTextPassword + "\n")
                    self.outputFile.flush()
                    self.bcrypt_hashes.remove(bcrypt_hash)
                    
                    if not self.bcrypt_hashes:
                        return True
            return False
        
        else:
            possiblePassword = self.getHash(plainTextPassword)  # ✅ Génération du hash ici
            for password in list(self.passwordList):
                if self.comparePasswords(possiblePassword, password):  # ✅ Comparaison directe
                    print(f"✅ Mot de passe trouvé : {plainTextPassword}")
                    self.numCracked += 1
                    self.outputFile.write(plainTextPassword + "\n")
                    self.outputFile.flush()
                    self.passwordList.remove(password)
                    
                if len(self.passwordList) == 0:
                    return True
                
            return False


    # Function to check if masks are set and perform mask attack
    def checkMask(self, plainTextPassword) -> bool:
        if not self.appendMask and not self.prependMask:
            return False
        if len(self.appendMask) != 0:
            self.maskAttack(self.appendMask, plainTextPassword)
        if len(self.prependMask) != 0:
            self.maskAttack(self.prependMask, "", plainTextPassword)
        return True
    
    # Function to try a single password
    def try_password(self, password):
        if self.passwordCheck(password):
            return True
        return False
    
    # Function to perform normal brute force attack
    def normalBruteForce(self, keyspace, min_length=0, max_length=1) -> bool:
        print("\n🚀 Lancement de l'attaque par brute force...\n")
        
        for i in range(min_length, max_length):
            for attempt in itertools.product(keyspace, repeat=i + 1):
                password = ''.join(attempt)
                if self.passwordCheck(password):
                    return True
        return False

    # Function to perform rule-based attack
    def ruleAttack(self, keyspace, min_length=0, max_length=1) -> bool:
        for i in range(min_length, max_length):
            for ruleString in self.ruleList:
                for attempt in itertools.product(keyspace, repeat=i + 1):
                    word = "".join(attempt)
                    transformedWords = self.ruleEnhancer(ruleString, [word])
                    for transformedWord in transformedWords:
                        if self.passwordCheck(transformedWord):
                            return True
        return False
    
    # Function to perform brute force attack with or without rules
    def bruteForce(self, keyspace, min_length=0, max_length=1):
        print("\n \t \t ==== > _Running Brute Force ... ")
        if len(self.ruleList) != 0:
            self.ruleAttack(keyspace, min_length, max_length)
        else:
            self.normalBruteForce(keyspace, min_length, max_length)
    
    # Function to create mask list from mask string
    def createMaskList(self, mask: str, *customFileName) -> list:
        maskList = []
        for i in range(0, len(mask), 2): 
            if mask[i:i+2] == "?l":  
                maskList.append(getFileInfo("Resources/lowercases.txt"))
            elif mask[i:i+2] == "?u": 
                maskList.append(getFileInfo("Resources/uppercases.txt"))
            elif mask[i:i+2] == "?d":  
                maskList.append(getFileInfo("Resources/digits.txt"))
            elif mask[i:i+2] == "?s":  
                maskList.append(getFileInfo("Resources/punctuations.txt"))
            elif mask[i:i+2] == "?L":  
                maskList.append(getFileInfo("Resources/lowercases_uppercases.txt"))
            elif mask[i:i+2] == "?ld":  
                maskList.append(getFileInfo("Resources/lowercases_digits.txt"))
            elif mask[i:i+2] == "?ud": 
                maskList.append(getFileInfo("Resources/uppercases_digits.txt"))
            elif mask[i:i+2] == "?a":  
                maskList.append(getFileInfo("Resources/letters_digits.txt"))
            elif mask[i:i+2] == "?A":  
                maskList.append(getFileInfo("Resources/letters_digits_punctuations.txt"))
            else:
                for j in range(10):  
                    if mask[i:i+2] == ("?" + str(j)):
                        try:
                            maskList.append(getFileInfo("Resources/" + customFileName[j] + ".txt"))
                        except IndexError:
                            print(f"Erreur : Fichier personnalisé introuvable pour {j}.")
                            continue
        return maskList
    
    # Function to perform mask attack
    def maskAttack(self, mask: str, prefix="", suffix="", *customFileName):
        print("Running Mask Attack ... ")
        maskList = self.createMaskList(mask, *customFileName)

        with ThreadPoolExecutor(max_workers=4) as executor:
            results = executor.map(
                self.passwordCheck,
                (prefix + "".join(combination) + suffix for combination in itertools.product(*maskList))
            ) 
            
            if any(results):
                print("f\n✅ Mot de passe trouvé avec Mask Attack 🎉\n")
                return True
        
        return False

    # Function to enhance words based on rules
    def ruleEnhancer(self, ruleString: str, wordList: list) -> list:
        ruleCounter = 0  
        while ruleCounter < len(ruleString):
            rule = ruleString[ruleCounter]
            ruleCounter += ruleCountList.get(rule, 1)  
            nextWordList = []

            for word in wordList:
                func = ruleList.get(rule, None)
                if func is None:
                    print(f"⚠️ Règle inconnue : {rule}")
                    continue  
                    
                if rule in ruleCountList and ruleCountList[rule] > 1:
                    args = ruleString[ruleCounter - ruleCountList[rule] + 1: ruleCounter]
                    transformedWord = func(word, *args)
                else:
                    transformedWord = func(word)

                if not self.checkMask(transformedWord):  
                    nextWordList.append(transformedWord)

                    if self.passwordCheck(transformedWord):
                        return True

            if not wordList:
                print("⚠️ Aucun mot de passe n'a pu être transformé avec les règles fournies.")
                return []
            else:
                wordList = nextWordList

        return wordList
    
    def dictionaryAttack(self, dictionaryFile: str) -> bool:
        print("\n🚀 Lancement de l'attaque par dictionnaire classique...\n")
        
        try:
            with open(dictionaryFile, 'r', encoding='latin-1') as file:
                for word in file:
                    word = word.strip()
                    if self.passwordCheck(word):
                        if len(self.passwordList) == 0 and len(self.bcrypt_hashes) == 0:
                            print("✅ Tous les mots de passe ont été trouvés via l'attaque par dictionaire.")
                            return True
                return False
            print("❌ Mot de passe non trouvé dans le dictionaire entée en paramètre")
            
        except FileNotFoundError:
            print(f"❌ Fichier dictionaire {dictionaryFile} introuvable")
            return False
    
    def customDictionaryAttack(self, baseWordlistFile: str, ruleString: str) -> bool:
        print("\n🚀 Lancement de l'attaque par dictionnaire customisé avec des règles...\n")

        try:
            # Chargement de la liste de base
            with open(baseWordlistFile, 'r', encoding='utf-8') as file:
                baseWords = [word.strip() for word in file]

            # Application des règles de transformation
            customWordlist = self.ruleEnhancer(ruleString, baseWords)

            # Vérification des mots transformés
            for word in customWordlist:
                if self.passwordCheck(word):
                    if len(self.passwordList) == 0 and len(self.bcrypt_hashes) == 0:
                        print("\n \t ✅ Tous les mots de passe ont été trouvés via l'attaque par dictionnaire customisé.\n")
                        return True

            print("\n \t ❌ Mot de passe non trouvé après transformation.\n")
            return False

        except FileNotFoundError:
            print(f"\n \t ❌ Fichier {baseWordlistFile} introuvable.\n")
            return False

        
    def hybridAttack(self, dictionaryFile: str, customWordlistFile: str, ruleString :str, keyspace :str, min_length :int, max_length :int, mask :str = ""):
        print("\n \t🔥 Lancement de l'attaque hybride (FULL ATTACK MODE)... 🔥")
        print("\n \t🔥 .................................................... 🔥")
        
        print("\n \t \t1️⃣ Étape 1 :🔎  Dictionnaire classique...")
        if self.dictionaryAttack(dictionaryFile):
            return True
        
        print("\n \t \t2️⃣ Étape 2 : 🔎 Dictionnaire customisé (avec transformations)...")
        if self.customDictionaryAttack(customWordlistFile, ruleString):
            return True
        
        if mask:
            print("\n \t \t3️⃣ Étape 3 :🔎 Attaque par masque...")
            if self.maskAttack(mask):
                return True
        
        print("\n \t \t⚡ Étape 4 : Brute Force en dernier recours...")
        if self.bruteForce(keyspace, min_length, max_length):
            return True
        
        print("❌ L'attaque hybride n'a pas permis de trouver tous les mots de passe.")
        return False
    
    