# La Sécurité Commence par des Mots de Passe Robustes 🔐  

## 📜 Introduction  

Les mots de passe sont la première ligne de défense contre les cyberattaques. Cependant, ils restent l'un des points faibles les plus exploités. Ce document a pour objectif de :  
- Sensibiliser les utilisateurs à l'importance des mots de passe robustes.  
- Expliquer les techniques utilisées par les attaquants pour compromettre des mots de passe.  
- Fournir des recommandations pour mieux se protéger.  

### 🌍 Pourquoi est-ce important ?  
Chaque année, des milliards de mots de passe sont compromis, exposant des données personnelles et professionnelles à des cyberattaques. Comprendre les vulnérabilités et adopter de bonnes pratiques est essentiel pour protéger vos comptes et informations.  

---

## 🔍 Méthodes Utilisées par les Attaquants  

### 1. Brute Force  
- **Principe** : Tester toutes les combinaisons possibles jusqu'à trouver le mot de passe correct.  
- **Pourquoi ça marche ?** Les mots de passe courts ou simples sont plus faciles à casser avec cette méthode.  
- **Exemple** :  
  - Un mot de passe de 8 caractères alphanumériques peut avoir jusqu’à **218 billions** de combinaisons.  
- **Limite** : Inefficace contre des mots de passe longs et complexes.  

### 2. Attaque par Dictionnaire  
- **Principe** : Utiliser une liste de mots courants pour deviner le mot de passe.  
- **Exemple de Wordlist** :  
  - [Rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/tag/data).  
- **Pourquoi ça marche ?** Beaucoup d'utilisateurs choisissent des mots de passe simples ou courants comme "123456" ou "password".  

### 3. Attaque par Masque  
- **Principe** : Tester des combinaisons basées sur des schémas probables (ex. : lettres suivies de chiffres).  
- **Exemple** : Un mot de passe comme "abc1234" suit un schéma commun.  

### 4. Extraction et Cassage de Hashes  
- **Principe** : Récupérer des mots de passe hachés depuis des bases de données compromises, puis les casser à l'aide d'outils comme **Hashcat** ou **John the Ripper**.  
- **Limite** : Les mots de passe correctement salés sont beaucoup plus difficiles à casser.  

---

## 🛡️ Conseils pour Protéger vos Mots de Passe  

### 1. Créez des Mots de Passe Longs et Complexes  
- **Astuce** : Utilisez une combinaison de lettres, chiffres, et caractères spéciaux.  
- **Exemple** : `Xj#8d@zLp&3q!`  

### 2. Utilisez un Gestionnaire de Mots de Passe  
- **Pourquoi ?** Ces outils permettent de créer et de stocker des mots de passe uniques pour chaque compte.  
- **Exemples Recommandés** :  
  - [Bitwarden](https://bitwarden.com/)  
  - [Dashlane](https://www.dashlane.com/)  
  - [LastPass](https://www.lastpass.com/)  

### 3. Activez l’Authentification Multi-Facteurs (MFA)  
- **Pourquoi ?** Même si votre mot de passe est compromis, un attaquant ne pourra pas accéder à votre compte sans le second facteur (ex. : code envoyé par SMS).  

### 4. Changez vos Mots de Passe Sensibles Régulièrement  
- **Conseil** : Mettez à jour les mots de passe de vos comptes critiques (email, banque) tous les 6 mois.  

### 5. Sensibilisez-vous et Restez Informé  
- **Vérifiez vos données** : Utilisez [Have I Been Pwned](https://haveibeenpwned.com/) pour savoir si vos informations ont été compromises.  
- **Apprenez les bonnes pratiques** : Suivez des formations courtes sur la cybersécurité.  

---

## 📚 Ressources  

### Outils Recommandés  
- **[Bitwarden Password Generator](https://bitwarden.com/password-generator/)** : Générateur de mots de passe robustes.  
- **[Have I Been Pwned](https://haveibeenpwned.com/)** : Service permettant de vérifier si vos données ont été exposées.  

### Wordlists  
- **[Rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/tag/data)** : Une des listes les plus populaires pour les attaques par dictionnaire.  

---

## 💡 Avertissement  

Ce document est strictement destiné à des fins éducatives. Toute utilisation malveillante des informations contenues ici est strictement interdite.  

---

## 📥 Téléchargez le Rapport Complet  
Vous pouvez également télécharger une version PDF du rapport [ici](./Rapport/password-security.pdf).  

