# Interface graphique pour le Password Cracker adapté à ton projet

from passwordCracker import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Définition de la classe du Menu principal
class Menu(QWidget):
    BRUTE_FORCE = 0
    MASK = 1

    def __init__(self):
        super().__init__()
        # Définition des variables
        self.inputFile = ""  # Fichier contenant les mots de passe ou hashes à cracker
        self.outputFile = ""  # Fichier pour stocker les mots de passe trouvés
        self.mode = Menu.BRUTE_FORCE  # Mode par défaut : Brute Force
        self.methodInput = ""  # Dictionnaire ou masque pour les attaques
        self.rules = ""  # Fichier contenant les règles
        self.appendMask = ""  # Masque ajouté à la fin
        self.prependMask = ""  # Masque ajouté au début

        self.setupUI()

    def setupUI(self):
        """Initialisation de l'interface graphique"""
        self.setGeometry(200, 20, 400, 300)
        self.setWindowTitle('Password Cracker')

        layout = QGridLayout()
        self.setLayout(layout)

        # Sélection de la méthode d'attaque
        methodGroup = QButtonGroup()
        
        bruteForceBtn = QRadioButton("Attaque par Brute Force")
        bruteForceBtn.setChecked(True)
        bruteForceBtn.methodNum = Menu.BRUTE_FORCE
        methodGroup.addButton(bruteForceBtn, 0)
        bruteForceBtn.toggled.connect(self.selectAttackMode)
        layout.addWidget(bruteForceBtn, 0, 0)

        maskAttackBtn = QRadioButton("Attaque par Masque")
        maskAttackBtn.methodNum = Menu.MASK
        methodGroup.addButton(maskAttackBtn, 1)
        maskAttackBtn.toggled.connect(self.selectAttackMode)
        layout.addWidget(maskAttackBtn, 0, 1)

        # Bouton pour ouvrir le fichier d'entrée
        inputBtn = QPushButton("Sélectionner fichier d'entrée", self)
        inputBtn.clicked.connect(self.getInputFile)
        layout.addWidget(inputBtn, 1, 0, 1, 2)

        # Bouton pour ouvrir le fichier de sortie
        outputBtn = QPushButton("Sélectionner fichier de sortie", self)
        outputBtn.clicked.connect(self.getOutputFile)
        layout.addWidget(outputBtn, 2, 0, 1, 2)

        # Mode hachage
        self.hashDropdown = QComboBox(self)
        self.hashDropdown.addItem("Aucun", QVariant(passwordCracker.NO_HASH))
        self.hashDropdown.addItem("SHA1", QVariant(passwordCracker.SHA1))
        self.hashDropdown.addItem("MD5", QVariant(passwordCracker.MD5))
        self.hashDropdown.addItem("bcrypt", QVariant(passwordCracker.BCRYPT))
        layout.addWidget(self.hashDropdown, 3, 0, 1, 2)

        # Bouton pour démarrer l'attaque
        startBtn = QPushButton("Démarrer le crack", self)
        startBtn.clicked.connect(self.startCrack)
        layout.addWidget(startBtn, 4, 0, 1, 2)

    def selectAttackMode(self):
        """Sélectionner le mode d'attaque"""
        radiobutton = self.sender()
        if radiobutton.isChecked():
            self.mode = radiobutton.methodNum

    def getInputFile(self):
        """Sélectionne le fichier d'entrée contenant les mots de passe"""
        filePath, _ = QFileDialog.getOpenFileName(self, 'Ouvrir un fichier', '', "Fichiers texte (*.txt)")
        if filePath:
            self.inputFile = filePath

    def getOutputFile(self):
        """Sélectionne le fichier où seront enregistrés les résultats"""
        filePath, _ = QFileDialog.getSaveFileName(self, 'Enregistrer sous', '', "Fichiers texte (*.txt)")
        if filePath:
            self.outputFile = filePath

    def startCrack(self):
        """Démarre le processus de cracking"""
        if not self.inputFile:
            print("⚠️ Vous devez sélectionner un fichier d'entrée contenant les mots de passe à cracker.")
            return
        if not self.outputFile:
            print("⚠️ Vous devez sélectionner un fichier de sortie pour enregistrer les mots de passe trouvés.")
            return

        cracker = passwordCracker(self.inputFile, self.outputFile)
        cracker.setHashNum(self.hashDropdown.currentData())

        print("🔍 Lancement de l'attaque...")

        if self.mode == Menu.BRUTE_FORCE:
            cracker.bruteForce("abcdefghijklmnopqrstuvwxyz", 4, 6)  # Exemple : brute force entre 4 et 6 caractères
        else:
            cracker.maskAttack("?l?l?l?l")  # Exemple : attaque par masque

        print("✅ Crack terminé ! Résultats enregistrés dans", self.outputFile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec_())
