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

    # Function to get hash of a password based on the selected hash type
    def getHash(self, password: str):
        if self.verbose:
            print(f"Trying to crack password: {password}")
        if self.hashNumber == passwordCracker.SHA1:
            return hashlib.sha1(password.encode('utf-8')).hexdigest()
        elif self.hashNumber == passwordCracker.MD5:
            return hashlib.md5(password.encode('utf-8')).hexdigest()
        return password
    
    # Function to compare passwords based on the selected hash type
    def comparePasswords(self, possiblePassword: str, password: str) -> bool:
        if self.hashNumber == passwordCracker.BCRYPT:
            try:
                return bcrypt.checkpw(possiblePassword.encode('utf-8'), password.encode('utf-8'))
            except ValueError as e:
                print(f"⚠️ Erreur : Mot de passe non valide pour BCRYPT : {password}")
                print(f"Error: {e}")
                return False
        return possiblePassword == password
    
    # Function to check if a plain text password matches any hashed password in the list
    def passwordCheck(self, plainTextPassword):
        possiblePassword = self.getHash(plainTextPassword)
        
        for password in self.passwordList:
            if self.comparePasswords(possiblePassword, password):
                print(f"\n✅ Mot de passe trouvé : {plainTextPassword} 🎉\n")
                self.numCracked += 1
                self.outputFile.write(plainTextPassword + "\n")
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
        for i in range(min_length, max_length):
            with ThreadPoolExecutor(max_workers=4) as executor:
                results = executor.map(self.passwordCheck, 
                                    (''.join(attempt) for attempt in itertools.product(keyspace, repeat=i+1)))
                if any(results):
                    return True  
        return False

    # Function to perform rule-based attack
    def ruleAttack(self, keyspace, min_length=0, max_length=1) -> bool:
        for i in range(min_length, max_length):
            for ruleString in self.ruleList:
                lengthAttempt = itertools.product(keyspace, repeat=i+1)
                generatedWords = ["".join(word) for word in lengthAttempt]
                
                transformedWords = self.ruleEnhancer(ruleString, generatedWords)
                
                for word in transformedWords:
                    if self.passwordCheck(word):
                        return True
        return False
    
    # Function to perform brute force attack with or without rules
    def bruteForce(self, keyspace, min_length=0, max_length=1):
        print("Running Brute Force ... ")
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
