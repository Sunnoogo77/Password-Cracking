import hashlib
import os

# ✅ Make sure the directory exists
os.makedirs("/Input", exist_ok=True)

# ✅ 10 common passwords from RockYou
passwords = [
    "anubhavjayaswal", "password", "grand_depok_city", "!(**SWEETHEART@@", "!&=&ciud70000560",
    "!!!@@3$$%%%", "iloveyou", "admin", "!!!!!!!##!(^^!@#!@#!@#!", "sunshine"
]

# ✅ Convert to SHA1
hashed_passwords = [hashlib.sha1(p.encode()).hexdigest() for p in passwords]

# ✅ Save to file
file_path = "/Input/dictionary_test.txt"
with open(file_path, "w", encoding="utf-8") as f:
    for h in hashed_passwords:
        f.write(h + "\n")

print(f"✅ SHA1 Password File Created: {file_path}")
print(hashed_passwords)
