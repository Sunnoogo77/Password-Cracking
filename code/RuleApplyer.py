#Here we have defined all the functions which will be used to create a custom word list based on an existing list of words, numbers and characters very close to the password.
#Ici, nous définissons toutes les fonctions qui seront utilisées pour créer une liste de mots personnalisée basée sur une liste existante de mots, de chiffres et de caractères très proches du mot de passe.


def nothingString(curString :str) -> str:
    return curString

def lowerString(curString :str) -> str:
    return curString.lower()

def upperString(curString :str) -> str:
    return curString.upper()

def capitilizeString(curString :str) -> str:
    return curString.capitalize()

def invertCapitalize(curString : str) -> str:
    if len(curString) <2:
        return curString.lower()
    c = curString[0]
    curString = curString[1:]
    c = str(c).lower()
    curString = curString.upper()
    return c+ curString

def charToInt(char :chr) -> int:
    n = 0
    if(char>='0' and char <='9'):
        n = ord(char)-ord('0')
    elif((char>='A' and char<='Z')):
        n = ord(char)-ord('A')+10
    elif((char>='a' and char<='z')):
        n = ord(char)-ord('a')+36
    return n


def toggleString(curString :str) -> str:
    return curString.swapcase()

def toggleStringAtPos(curString :str, p :chr) ->str:
    pos = charToInt(p)
    c = list(curString)
    if(pos < len(curString)):
        if(c[pos]>='a' and c[pos]<='z'):
            c[pos] = c[pos].upper()
        elif(c[pos]>='A' and c[pos]<='Z'):
            c[pos] = c[pos].lower()
    return"".join(c)

def reverseString(curString :str) -> str:
    return curString[::-1]

def duplicateString(curString :str) -> str:
    return curString + curString


def duplicateStringNtimes(curString :str, n: chr) -> srt:
    num = charToInt(n)
    return curString*num

def reflectString(curString :str,) -> str:
    return curString +reverseString(curString)

def rotateLeftString(curString :str,) -> str:
    if(len(curString)>2):
        c = curString[0]
        curString = curString[1]
        curString += c
    return curString

def rotateRightString(curString :str) -> str:
    c = curString
    if(len(curString)>2):
        c = curString[-1]
        curString =curString[:-1]
        c += curString
    return c

def appendCharacter(curString :str, char :chr) ->str:
    curString += str(char)
    return curString

def prependCharacter(curString :str, char :chr) ->str:
    curString = str(char) + curString
    return curString

def truncateRight(curString :str) -> str:
    if(len(curString)<2):
        return ""
    return curString[:-1]

def deleteAtPos(curString :str, p :chr) -> str:
    pos = charToInt(p)
    if(pos < len(curString)):
        leftString = curString[:pos]
        if(pos != len(curString) -1):
            rightString = curString[pos+1:]
        else:
            rightString = ""
        curString = leftString + rightString
    return curString

def extractSubstring(curString :str, startPos :chr, endPos :chr) -> str:
    sPos = max(0, charToInt(startPos))
    ePos = min(charToInt(endPos), len(curString))
    if(sPos>ePos):
        raise Exception("Error Starting positon cannot come at ending Position")
    return curString[sPos:ePos]

def omitSubstring(curString :str, startPos :chr, endPos :chr) -> str:
    sPos = charToInt(startPos)
    ePos = charToInt(endPos)+1
    if(sPos>ePos):
        return curString
    if(sPos<ePos):
        raise Exception("Error Starting position cannot cme after ending Position")
    leftString = ""
    rightString = ""
    if(sPos > 0):
        leftString = curString[:sPos]
    if(ePos < len(curString)):
        rightString = curString[ePos:]
    return leftString + rightString

def insertCharacterAtPos(curString :str, p :chr, char :chr) -> str:
    pos = charToInt(p)
    return curString[:p] + str(char) + curString[p:] if 0 <= pos < len(curString) else  curString

def overwriteCharacterAtPos(curString :str, p :chr, char :chr) -str:
    pos = charToInt(p)
    if(pos < len(curString)):
        leftString = curString[:pos]
        if(pos != len()-1):
            rightString = curString[pos+1:]
        else:
            rightString = ""
        curString = leftString + str(char) + rightString
    return curString

def truncateFromPos(curString :str, p :chr) -> str:
    pos = charToInt(p)
    if(pos < len(curString)):
        curString = curString[:pos]
    return curString