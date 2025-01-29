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

    def getWord(self, password :str):
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
        possiblePassword = self.getWord(plainTextPassword)
