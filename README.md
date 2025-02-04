# 🔐 **La Sécurité Commence par des Mots de Passe Robustes**  

## 📜 **Objectif du Projet**  
Ce projet vise à sensibiliser les utilisateurs à l'importance des mots de passe robustes pour protéger leurs données personnelles et professionnelles.  
Il repose sur deux volets principaux :  
1. **Un rapport éducatif** sur la sécurité des mots de passe.  
2. **Un outil de crackage de mots de passe** développé pour illustrer les techniques d'attaque et tester la robustesse des mots de passe.  

---

## 📂 **Contenu du Dépôt**  

### 📄 **1. Rapport Principal**  
- **[Rapport de Sécurité des Mots de Passe](Rapport/password-security.pdf)** :  
  Un document complet qui explore :  
  - Les méthodes utilisées par les attaquants pour compromettre les mots de passe.  
  - Pourquoi ces méthodes fonctionnent.  
  - Les bonnes pratiques pour renforcer la sécurité des mots de passe.  

---

### 💻 **2. Outil de Crackage de Mots de Passe**  
Un outil développé en Python permettant de simuler différentes techniques d'attaque sur des mots de passe :  
- **Attaque par Brute Force**  
- **Attaque par Dictionnaire**  
- **Attaque par Dictionnaire Personnalisé (Custom Dictionary)**  
- **Attaque par Masque**  
- **Attaque Hybride (combinaison de plusieurs méthodes)**  

👉 **Accéder à l'outil :** [Dossier de l'Outil Password Cracker](code) *(renommer si besoin)*  
L'outil est accompagné d'une interface graphique pour faciliter son utilisation.  

---

### 🗂️ **3. Ressources Utiles**  
- **[Tools.md](Resources/tools.md)** : Liste des outils recommandés (gestionnaires, générateurs de mots de passe, etc.).  
- **[References.md](Resources/references.md)** : Références académiques et ressources pour approfondir le sujet.  
- **[Wordlists.md](Resources/wordlists.md)** : Informations sur les listes de mots de passe courants utilisées par les attaquants.  

---

## ⚙️ **Structure du Dépôt**  
```
Password-Cracking/
├── Rapport/                 # Rapport d'étude sur la sécurité des mots de passe
│   ├── password-security.md
│   └── password-security.pdf
├── Resources/               # Outils, références et wordlists
│   ├── tools.md
│   ├── references.md
│   └── wordlists.md
├── PasswordCracker  # Outil de crackage de mots de passe
│   ├── main.py
│   ├── passwordCracker.py
│   ├── RuleApplyer.py
│   ├── CreatCharacter.py
│   ├── Input/
│   ├── Output/
│   ├── diagrams/            # Diagrammes UML (Use Case, Classes, Séquences)
│   └── Resources/           # Fichiers pour les attaques par masque et dictionnaire
└── README.md                # Ce fichier
```

---

## 🛠️ **Technologies et Outils**  
- **Langage :** Python 3  
- **Bibliothèques :** PyQt5, bcrypt, hashlib, itertools, etc.  
- **Interface Graphique :** Développée avec PyQt5  
- **Diagrammes UML :** Pour illustrer l'architecture de l'outil (dans `code/diagrams/`)  

---

## 🚀 **Comment Utiliser l'Outil ?**  
1. Accédez au dossier [code](code).  
2. Consultez le **README dédié à l'outil** pour des instructions détaillées sur l'installation, la configuration et l'utilisation.  

---

## 📊 **Ressources Annexes**  
- **Générateur de mots de passe sécurisé :** [Bitwarden Password Generator](https://bitwarden.com/password-generator/)  
- **Vérifiez si vos données ont été compromises :** [Have I Been Pwned](https://haveibeenpwned.com/)  

---

## ⚠️ **Avertissement**  
Ce projet est uniquement destiné à des fins **éducatives** et de **sensibilisation à la cybersécurité**.  
Toute utilisation malveillante des informations ou de l'outil développé est **strictement interdite**.  
**Utilisez cet outil de manière responsable et légale.**  

