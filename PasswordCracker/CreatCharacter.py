import string
import os

#Création de fichier avec la liste des Charactères
def generate_chars_file(file_name: str, char_list: str):
    """"
    Génère un fichier contenant les caractères, un par ligne
    """
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    
    os.makedirs("Resources", exist_ok=True)
    
    with open(f"Resources/{file_name}", "w", encoding="utf-8") as file:
        for char in char_list:
            file.write(char + "\n")
    print(f"Fichier {file_name} généré avec succès dans Ressources/{file_name}")


#Génération des fichiers necessaires
def generate_characer_files():
    """
    Génère les fichiers predefinis pour les attaques par Brute Force
    """
    print("Génération des fichiers de caractères...")
    
    #fichier simple
    generate_chars_file("lowercases", string.ascii_lowercase) #Lettres miniscules
    generate_chars_file("uppercases", string.ascii_uppercase) #Lettres majuscules
    generate_chars_file("digits", string.digits) #Chiffres
    generate_chars_file("punctuations", string.punctuation) #Ponctuations
    generate_chars_file("lowercases_uppercases", string.ascii_letters) #Lettres miniscules et majuscules
    generate_chars_file("lowercases_digits", string.ascii_lowercase + string.digits) #Lettres miniscules et chiffres
    generate_chars_file("uppercases_digits", string.ascii_uppercase + string.digits) #Lettres majuscules et chiffres
    generate_chars_file("letters_digits", string.ascii_letters + string.digits) # Toutes lettres + chiffres
    generate_chars_file("letters_digits_punctuations", string.ascii_letters + string.digits + string.punctuation) #Toutes lettres + chiffres + ponctuations
    
    print("[DONE]  Tous les fichiers ont été générés dans le dossier 'Resources/'.")
    


# Appeler la fonction pour générer les fichiers
if __name__ == "__main__":
    generate_characer_files()
