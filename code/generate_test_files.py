# import hashlib
# import bcrypt
# import os

# # Directory for test files
# os.makedirs("test_files", exist_ok=True)

# ### 📌 1. Passwords File (Plaintext & Hashed) ###
# plaintext_passwords = ["hello", "password123", "admin", "qwerty", "letmein"]
# sha1_hashes = [hashlib.sha1(p.encode()).hexdigest() for p in plaintext_passwords]
# md5_hashes = [hashlib.md5(p.encode()).hexdigest() for p in plaintext_passwords]
# bcrypt_hashes = [bcrypt.hashpw(p.encode(), bcrypt.gensalt()).decode() for p in plaintext_passwords]

# with open("test_files/passwords.txt", "w", encoding="utf-8") as f:
#     f.write("# Plaintext Passwords\n")
#     f.writelines(f"{p}\n" for p in plaintext_passwords)
    
#     f.write("\n# SHA1 Hashes\n")
#     f.writelines(f"{h}\n" for h in sha1_hashes)

#     f.write("\n# MD5 Hashes\n")
#     f.writelines(f"{h}\n" for h in md5_hashes)

#     f.write("\n# BCRYPT Hashes\n")
#     f.writelines(f"{h}\n" for h in bcrypt_hashes)

# print("✅ Created test_files/passwords.txt")


# ### 📌 2. Rules File ###
# rules = [
#     "u",  # Uppercase all
#     "l",  # Lowercase all
#     "r",  # Reverse string
#     "d",  # Duplicate string
#     "t",  # Toggle case
#     "^$", # Add '$' at the beginning
#     "$1"  # Add '1' at the end
# ]

# with open("test_files/rules.txt", "w", encoding="utf-8") as f:
#     f.writelines(f"{r}\n" for r in rules)

# print("✅ Created test_files/rules.txt")


# ### 📌 3. Mask File ###
# masks = [
#     "?l?l?l?l?l",  # Lowercase 5 letters
#     "?u?l?d?d?d",  # Uppercase letter, lowercase letter, digit, digit, digit
#     "?a?a?a?a"      # Any printable character (4 chars)
# ]

# with open("test_files/masks.txt", "w", encoding="utf-8") as f:
#     f.writelines(f"{m}\n" for m in masks)

# print("✅ Created test_files/masks.txt")


import hashlib
import bcrypt
import os

# Directory for test files
os.makedirs("test_cases", exist_ok=True)

# Sample passwords
plaintext_passwords = ["hello", "password123", "admin", "qwerty", "letmein"]

# Create SHA1, MD5, and BCRYPT hashes
sha1_hashes = [hashlib.sha1(p.encode()).hexdigest() for p in plaintext_passwords]
md5_hashes = [hashlib.md5(p.encode()).hexdigest() for p in plaintext_passwords]
bcrypt_hashes = [bcrypt.hashpw(p.encode(), bcrypt.gensalt()).decode() for p in plaintext_passwords]

### 📌 1. Brute Force Test (Plaintext) ###
with open("test_cases/password_plain.txt", "w", encoding="utf-8") as f:
    f.writelines(f"{p}\n" for p in plaintext_passwords)
print("✅ Created test_cases/password_plain.txt")

### 📌 2. SHA1 Hash Test ###
with open("test_cases/password_sha1.txt", "w", encoding="utf-8") as f:
    f.writelines(f"{h}\n" for h in sha1_hashes)
print("✅ Created test_cases/password_sha1.txt")

### 📌 3. MD5 Hash Test ###
with open("test_cases/password_md5.txt", "w", encoding="utf-8") as f:
    f.writelines(f"{h}\n" for h in md5_hashes)
print("✅ Created test_cases/password_md5.txt")

### 📌 4. BCRYPT Hash Test ###
with open("test_cases/password_bcrypt.txt", "w", encoding="utf-8") as f:
    f.writelines(f"{h}\n" for h in bcrypt_hashes)
print("✅ Created test_cases/password_bcrypt.txt")

### 📌 5. Rules File ###
rules = [
    "u",  # Uppercase all
    "l",  # Lowercase all
    "r",  # Reverse string
    "d",  # Duplicate string
    "t",  # Toggle case
    "^$", # Add '$' at the beginning
    "$1"  # Add '1' at the end
]
with open("test_cases/rules.txt", "w", encoding="utf-8") as f:
    f.writelines(f"{r}\n" for r in rules)
print("✅ Created test_cases/rules.txt")

### 📌 6. Masks File ###
masks = [
    "?l?l?l?l?l",  # Lowercase 5 letters
    "?u?l?d?d?d",  # Uppercase letter, lowercase letter, digit, digit, digit
    "?a?a?a?a"      # Any printable character (4 chars)
]
with open("test_cases/masks.txt", "w", encoding="utf-8") as f:
    f.writelines(f"{m}\n" for m in masks)
print("✅ Created test_cases/masks.txt")
