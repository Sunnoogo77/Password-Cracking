def create_character_file(output_file, include_lowercase=True, include_uppercase=True, include_digits=True, include_special=True):
    chars = ""
    if include_lowercase:
        chars += "abcdefghijklmnopqrstuvwxyz"
    if include_uppercase:
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if include_digits:
        chars += "0123456789"
    if include_special:
        chars += "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        
    with open(output_file, 'w') as f:
        for char in chars:
            f.write(char + "\n")
    print(f"Fichier de caractères créé: {output_file}")
    
if __name__ == "__main__":
    create_character_file("Output/chars.txt", include_lowercase=True, include_uppercase=True, include_digits=True, include_special=True)