import itertools
from RuleApplyer import *
from urllib.request import urlopen, hashlib
import hashlib
import bcrypt


def getFileInfo(filePath :str):
    with open(filePath, "r") as file:
        return file.read().splitlines()


class passwordCracker:
    NO_HASH = 0
    SHA1 = 1
    MD5 = 2
    BCRYPT = 3
    
    def __init__(self, inputPasswordFile :str, oFile :str):
        self.passwordList = getFileInfo(inputPasswordFile)
        self.outputFile = open(oFile, "w+", encoding="utf-8")
        self.hashNumber = passwordCracker.NO_HASH
        self.verbose = False
        self.appendMask = []
        self.prependMask = []
        self.ruleList = []
        self.numCracked = 0

    def setHashNum(self, num :int):
        self.hashNumber = num
    
    def setVerboseMode(self, verboseMode :bool):
        self.verbose = verboseMode
    
    def getHash(self, password :str):
        if(self.verbose):
            print(f"Trying to crack password: {password}")
        if self.hashNumber == passwordCracker.SHA1:
            return hashlib.sha1(password.encode('utf-8')).hexdigest()
        elif self.hashNumber == passwordCracker.MD5:
            return hashlib.md5(password.encode('utf-8')).hexdigest()
        return password
    
    def comparePasswords(self, possiblePassword :str, password :str):
        if (self.hashNumber == passwordCracker.BCRYPT):
            try:
                return bcrypt.checkpw(possiblePassword.encode('utf-8'), password.encode('utf-8'))
            except ValueError as e:
                print(f"Error: {e}")
                return False
        return possiblePassword == password
    
    def passwordCheck(self, plainTextPassword):
        possiblePassword = self.getHash(plainTextPassword)
        
        for password in self.passwordList:
            if self.comparePasswords(possiblePassword, password):
                print("-- :) --- Cracked: " + plainTextPassword)
                self.numCracked += 1
                self.outputFile.write(plainTextPassword+"\n")
                self.passwordList.remove(password)
                
            if len(self.passwordList) == 0:
                return True
        return False

    
    def setAppendMask(self, am :str):
        self.appendMask = am
    
    def setPrependMask(self, pm :str):
        self.prependMask = pm
    
    def checkMask(self, plainTextPassword) -> bool:
        if(len(self.appendMask) == 0 and len(self.prependMask) == 0):
            return False
        if(len(self.appendMask) != 0):
            self.maskAttack(self.appendMask, plainTextPassword)
        if(len(self.prependMask) != 0):
            self.maskAttack(self.prependMask, "", plainTextPassword)
        return True
    
    def setRuleList(self, rl :list):
        self.ruleList = rl
    
    
    def normalBruteForce(self, keyspace, min_length=0, max_length=1) -> bool:
        for i in range(min_length, max_length):
            lengthAttempt = itertools.product(keyspace, repeat=i+1)
            for attempt in lengthAttempt:
                plainTextPassword = ''.join(attempt)
                
                if not self.checkMask(plainTextPassword):
                    if self.passwordCheck(plainTextPassword):
                        return True
        return False
    
    def ruleAttack(self, keyspace, min_length=0, max_length=1) -> bool:
        for i in range(min_length, max_length):
            for ruleString in self.ruleList:
                lengthAttempt = itertools.product(keyspace, repeat=i+1)
                generatedWords = ["".join(word) for word in lengthAttempt]
                
                transformedWords = self.applyRules(generatedWords, ruleString)
                
                for word in transformedWords:
                    if self.passwordCheck(word):
                        return True
        return False
    
    def bruteForce(self, keyspace, min_length=0, max_length=1):
        print("Running Brute Force ... ")
        if len(self.ruleList) != 0:
            self.ruleAttack(keyspace, min_length, max_length)
        else:
            self.normalBruteForce(keyspace, min_length, max_length)
    
    
    

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
                            maskList.append(getFileInfo("Resources/"+customFileName[j]+".txt"))
                        except IndexError:
                            print(f"Erreur : Fichier personnalisé introuvable pour {j}.")
                            continue

        return maskList
    
    def createMaskScript(self, maskList: list, prefix="", suffix="") -> str:
        s = ""
        variableList = getFileInfo("Resources/lowercases_uppercases.txt")

        for i in range(len(maskList)):
            var_name = variableList[i % len(variableList)]
            s += f"for {var_name} in maskList[{i}]:\n"
            s += "\t" * (i+1)
        
        s += "plainTextPassword =  " + " + ".join(
            [variableList[i % len(variableList)] for i in range(len(maskList))]
        ) + "\n"
        
        s += "\t" * len(maskList) + f"if self.passwordCheck(prefix + plainTextPassword + suffix):\n"
        s += "\t" * (len(maskList)+1) + "exit()\n"
        
        return s
    
    def maskAttack(self, mask: str, prefix="", suffix="", *customFileName):
        print("Running Mask Attack ... ")
        maskList = self.createMaskList(mask, customFileName)

        for combination in itertools.product(*maskList):  
            plainTextPassword = prefix + "".join(combination) + suffix
            if self.passwordCheck(plainTextPassword):
                return True  

    
    def applyRules(self, wordList: list, ruleString: str) -> list:
        transformedWords = []

        for word in wordList:
            transformedWord = word  # Mot de départ

            for rule in ruleString:
                if rule == "u":  # Mettre en majuscules
                    transformedWord = transformedWord.upper()
                elif rule == "l":  # Mettre en minuscules
                    transformedWord = transformedWord.lower()
                elif rule == "r":  # Inverser le mot
                    transformedWord = transformedWord[::-1]
                elif rule == "d":  # Dupliquer
                    transformedWord = transformedWord + transformedWord
                elif rule == "T":  # Inverser la casse à une position spécifique
                    position = 2  # Exemple : on pourrait rendre ça dynamique
                    transformedWord = toggleStringAtPos(transformedWord, str(position))

                elif rule == "t":  # Inverser la casse (toggle case)
                    transformedWord = ''.join(
                        c.upper() if c.islower() else c.lower() for c in transformedWord
                    )
                elif rule == "$":  # Ajouter un caractère à la fin
                    transformedWord += "!"
                elif rule == "^":  # Ajouter un caractère au début
                    transformedWord = "@" + transformedWord
                else:
                    print(f"⚠️ Règle inconnue : {rule}")

            transformedWords.append(transformedWord)

        return transformedWords

    
    