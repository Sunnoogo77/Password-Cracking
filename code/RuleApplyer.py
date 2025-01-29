#Here we have defined all the functions which will be used to create a custom word list based on an existing list of words, numbers and characters very close to the password.
#Ici, nous définissons toutes les fonctions qui seront utilisées pour créer une liste de mots personnalisée basée sur une liste existante de mots, de chiffres et de caractères très proches du mot de passe.


def nothingString(curString: str) -> str:
    # No transformation
    return curString

def lowerString(curString: str) -> str:
    # Convert to lowercase
    return curString.lower()

def upperString(curString: str) -> str:
    # Convert to uppercase
    return curString.upper()

def capitilizeString(curString: str) -> str:
    # Capitalize the first letter
    return curString.capitalize()

def invertCapitalize(curString: str) -> str:
    # Invert capitalization
    if len(curString) < 2:
        return curString.lower()
    c = curString[0]
    curString = curString[1:]
    c = str(c).lower()
    curString = curString.upper()
    return c + curString

def charToInt(char: chr) -> int:
    # Convert character to integer
    n = 0
    if '0' <= char <= '9':
        n = ord(char) - ord('0')
    elif 'A' <= char <= 'Z':
        n = ord(char) - ord('A') + 10
    elif 'a' <= char <= 'z':
        n = ord(char) - ord('a') + 36
    return n

def toggleString(curString: str) -> str:
    # Toggle case of all characters
    return curString.swapcase()

def toggleStringAtPos(curString: str, p: chr) -> str:
    # Toggle case at a specific position
    pos = charToInt(p)
    c = list(curString)
    if pos < len(curString):
        if 'a' <= c[pos] <= 'z':
            c[pos] = c[pos].upper()
        elif 'A' <= c[pos] <= 'Z':
            c[pos] = c[pos].lower()
    return "".join(c)

def reverseString(curString: str) -> str:
    # Reverse the string
    return curString[::-1]

def duplicateString(curString: str) -> str:
    # Duplicate the string
    return curString + curString

def duplicateStringNtimes(curString: str, n: chr) -> str:
    # Duplicate the string N times
    num = charToInt(n)
    return curString * num

def reflectString(curString: str) -> str:
    # Reflect the string
    return curString + reverseString(curString)

def rotateLeftString(curString: str) -> str:
    # Rotate the string to the left
    if len(curString) > 1:
        c = curString[0]
        curString = curString[1:] + c
    return curString

def rotateRightString(curString: str) -> str:
    # Rotate the string to the right
    if len(curString) > 1:
        c = curString[-1]
        curString = c + curString[:-1]
    return curString

def appendCharacter(curString: str, char: chr) -> str:
    # Append a character
    return curString + str(char)

def prependCharacter(curString: str, char: chr) -> str:
    # Prepend a character
    return str(char) + curString

def truncateRight(curString: str) -> str:
    # Truncate the string from the right
    if len(curString) < 2:
        return ""
    return curString[:-1]

def deleteAtPos(curString: str, p: chr) -> str:
    # Delete character at a specific position
    pos = charToInt(p)
    if pos < len(curString):
        curString = curString[:pos] + curString[pos+1:]
    return curString

def extractSubstring(curString: str, startPos: chr, endPos: chr) -> str:
    # Extract a substring
    sPos = max(0, charToInt(startPos))
    ePos = min(charToInt(endPos), len(curString))
    if sPos > ePos:
        raise Exception("Error: Starting position cannot come after ending position")
    return curString[sPos:ePos]

def omitSubstring(curString: str, startPos: chr, endPos: chr) -> str:
    # Omit a substring
    sPos = charToInt(startPos)
    ePos = charToInt(endPos) + 1
    if sPos > ePos:
        return curString
    if sPos < ePos:
        raise Exception("Error: Starting position cannot come after ending position")
    return curString[:sPos] + curString[ePos:]

def insertCharacterAtPos(curString: str, p: chr, char: chr) -> str:
    # Insert a character at a specific position
    pos = charToInt(p)
    return curString[:pos] + str(char) + curString[pos:] if 0 <= pos < len(curString) else curString

def overwriteCharacterAtPos(curString: str, p: chr, char: chr) -> str:
    # Overwrite character at a specific position
    pos = charToInt(p)
    if pos < len(curString):
        curString = curString[:pos] + str(char) + curString[pos+1:]
    return curString

def truncateFromPos(curString: str, p: chr) -> str:
    # Truncate the string from a specific position
    pos = charToInt(p)
    if pos < len(curString):
        curString = curString[:pos]
    return curString

def replaceCharacter(curString: str, oldChar: chr, newChar: chr) -> str:
    # Replace a character
    return curString.replace(oldChar, newChar)

def purgeString(curString: str, char: chr) -> str:
    # Remove all instances of a character
    return curString.replace(char, "")

def duplicateFirst(curString: str) -> str:
    # Duplicate the first character
    return curString[0] + curString

def duplicateFirstNChars(curString: str, n: chr) -> str:
    # Duplicate the first N characters
    num = charToInt(n)
    if num < len(curString):
        curString = curString[:num] + curString
    return curString

def duplicateLast(curString: str) -> str:
    # Duplicate the last character
    return curString + curString[-1]

def duplicateAll(curString: str) -> str:
    # Duplicate all characters
    return "".join([c*2 for c in curString])

#Rule list
# Dictionary mapping rule symbols to their corresponding functions
ruleList = {
    ":": nothingString,          # No transformation
    "l": lowerString,            # Convert to lowercase
    "u": upperString,            # Convert to uppercase
    "c": capitilizeString,       # Capitalize the first letter
    "C": invertCapitalize,       # Invert capitalization
    "t": toggleString,           # Toggle case of all characters
    "T": toggleStringAtPos,      # Toggle case at a specific position
    "r": reverseString,          # Reverse the string
    "d": duplicateString,        # Duplicate the string
    "D": duplicateStringNtimes,  # Duplicate the string N times
    "R": reflectString,          # Reflect the string
    "L": rotateLeftString,       # Rotate the string to the left
    "R": rotateRightString,      # Rotate the string to the right
    "a": appendCharacter,        # Append a character
    "p": prependCharacter,       # Prepend a character
    "t": truncateRight,          # Truncate the string from the right
    "D": deleteAtPos,            # Delete character at a specific position
    "E": extractSubstring,       # Extract a substring
    "O": omitSubstring,          # Omit a substring
    "I": insertCharacterAtPos,   # Insert a character at a specific position
    "O": overwriteCharacterAtPos,# Overwrite character at a specific position
    "T": truncateFromPos,        # Truncate the string from a specific position
    "R": replaceCharacter,       # Replace a character
    "P": purgeString,            # Remove all instances of a character
    "F": duplicateFirst,         # Duplicate the first character
    "N": duplicateFirstNChars,   # Duplicate the first N characters
    "L": duplicateLast,          # Duplicate the last character
    "A": duplicateAll            # Duplicate all characters
}

# Dictionary mapping rule symbols to the number of arguments they require
ruleCountList = {
    "D": 1,  # Duplicate string N times requires 1 argument
    "D": 2,  # Delete character at a specific position requires 1 argument
    "T": 1,  # Toggle case at a specific position requires 1 argument
    "E": 2,  # Extract a substring requires 2 arguments
    "O": 2,  # Omit a substring requires 2 arguments
    "I": 2,  # Insert a character at a specific position requires 2 arguments
    "O": 2,  # Overwrite character at a specific position requires 2 arguments
    "N": 1   # Duplicate the first N characters requires 1 argument
}
