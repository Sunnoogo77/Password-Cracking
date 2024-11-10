# Password-Cracking-Project


## Introduction
Les mots de passe sont souvent la première ligne de défense pour protéger les données sensibles, mais ils peuvent aussi être une vulnérabilité majeure si leur sécurité est faible. Ce projet explore différentes techniques de cassage de mots de passe, afin de comprendre comment les mots de passe peuvent être compromis et comment améliorer les pratiques de sécurité. Ce projet est strictement à des fins éducatives et est réalisé dans un environnement sécurisé.

> **Note de sécurité** : Ce projet n'est pas destiné à des activités malveillantes. Il vise à sensibiliser sur les faiblesses des mots de passe et à encourager l'utilisation de mots de passe plus robustes.

## Objectifs du Projet
- Comprendre les différentes techniques de cassage de mots de passe.
- Appliquer des méthodes comme le brute-force, l’attaque par dictionnaire, et les attaques par masque pour casser des mots de passe simples.
- Étudier les méthodes d’attaque de mots de passe hashés pour sensibiliser sur la sécurité de stockage des mots de passe.

## Contenu du Projet
Ce projet est divisé en trois parties principales, chaque partie étant conçue pour simuler une technique de cassage de mots de passe spécifique.

### Partie 1 : Attaque Brute Force
Le brute force consiste à tester toutes les combinaisons possibles pour trouver le mot de passe. Bien que cette méthode soit souvent lente, elle est fiable car elle tente chaque possibilité.
- **Exemple de code** : Un script Python qui essaie toutes les combinaisons de caractères jusqu'à une longueur définie.
- **Limites** : Lent pour les mots de passe complexes ou longs.

### Partie 2 : Attaque par Dictionnaire
L'attaque par dictionnaire utilise des listes de mots de passe courants pour deviner le mot de passe. Cette méthode est plus rapide que le brute force pour les mots de passe faibles ou fréquents.
- **Exemple de code** : Un script Python qui parcourt une wordlist et teste chaque mot comme potentiel mot de passe.
- **Personnalisation** : Peut être améliorée en utilisant des wordlists adaptées à la cible.

### Partie 3 : Attaques Améliorées (Masque et Hybride)
- **Attaque par Masque** : Limite le test aux caractères probables (ex. lettres suivies de chiffres), ce qui accélère le processus.
- **Attaque Hybride** : Combine dictionnaire et brute force pour tester des mots suivis de chiffres ou de caractères spéciaux.
- **Exemple de code** : Scripts Python pour tester des variations de mots de passe avec des masques et des règles spécifiques.

### Partie 4 : Attaques de Hashes
Cette partie explore comment casser des mots de passe hashés, en utilisant des techniques comme les tables arc-en-ciel pour les hashes non salés.
- **Outils externes** : Utilisation de Hashcat ou d'autres outils de décodage pour casser des mots de passe hashés.

## Installation et Exécution
### Prérequis
- **Python 3** : Utilisé pour les scripts de cassage de mots de passe.
- **Wordlist** : Vous pouvez télécharger une wordlist, comme [Rockyou](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt), pour les tests d'attaque par dictionnaire.

### Instructions
1. **Clonez ce dépôt** :
   ```bash
   git clone https://github.com/votre_nom/password-cracking-project.git
