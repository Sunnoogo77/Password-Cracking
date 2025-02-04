from passwordCracker import *
from CreatCharacter import *
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Fonction pour charger un keyspace depuis un fichier
def loadKeyspaceFromFile(filePath: str) -> str:
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            keyspace = ''.join(line.strip() for line in file if line.strip())
        return keyspace
    except FileNotFoundError:
        print(f"❌ Fichier {filePath} introuvable.")
        return ""


# Thread pour exécuter l'attaque sans bloquer l'interface
class CrackingWorker(QThread):
    update_signal = pyqtSignal(str)

    def __init__(self, cracker, mode, keyspace, min_length, max_length, maskStr, dictionaryFile, customWordlistFile, ruleString):
        super().__init__()
        self.cracker = cracker
        self.mode = mode
        self.keyspace = keyspace
        self.min_length = min_length
        self.max_length = max_length
        self.maskStr = maskStr
        self.dictionaryFile = dictionaryFile
        self.customWordlistFile = customWordlistFile
        self.ruleString = ruleString

    def run(self):
        self.update_signal.emit("🔍 Démarrage de l'attaque...\n")

        if self.mode == Menu.BRUTE_FORCE:
            self.cracker.bruteForce(self.keyspace, self.min_length, self.max_length)

        elif self.mode == Menu.DICTIONARY:
            self.cracker.dictionaryAttack(self.dictionaryFile)

        elif self.mode == Menu.CUSTOM_DICTIONARY:
            self.cracker.customDictionaryAttack(self.customWordlistFile, self.ruleString)
        
        elif self.mode == Menu.MASK:
            self.cracker.maskAttack(self.maskStr)

        elif self.mode == Menu.HYBRID:
            self.cracker.hybridAttack(
                self.dictionaryFile,
                self.customWordlistFile,
                self.ruleString,
                self.keyspace,
                self.min_length,
                self.max_length,
                self.maskStr
            )

        self.update_signal.emit(f"✅ Crack completed! Results are saved file you entered as output file")


# Interface Graphique
class Menu(QWidget):
    BRUTE_FORCE = 0
    DICTIONARY = 1
    CUSTOM_DICTIONARY = 2
    HYBRID = 3
    MASK = 4

    def __init__(self):
        super().__init__()
        self.inputFile = ""
        self.outputFile = ""
        self.mode = Menu.BRUTE_FORCE
        self.methodInput = ""
        self.rules = ""
        self.appendMask = ""
        self.prependMask = ""
        self.dictionaryFile = ""
        self.customWordlistFile = ""
        self.ruleString = ""
        self.maskStr = ""

        self.setupUI()

    def setupUI(self):
        
        self.setWindowTitle("Password Cracker")  # Titre de la fenêtre
        layout = QVBoxLayout()  # Layout principal vertical
        self.setLayout(layout)

        # Groupe pour les modes d'attaque
        attack_group_box = QGroupBox("Mode d'attaque")
        attack_layout = QGridLayout()
        attack_group_box.setLayout(attack_layout)
        layout.addWidget(attack_group_box)

        self.methodGroup = QButtonGroup()
        attack_modes = [("Brute Force", Menu.BRUTE_FORCE), ("Dictionnaire", Menu.DICTIONARY),
                    ("Custom Dictionnaire", Menu.CUSTOM_DICTIONARY), ("Mask Attack", Menu.MASK), ("Hybride", Menu.HYBRID)]

        for i, (label, mode) in enumerate(attack_modes):
            radio_button = QRadioButton(label)
            radio_button.methodNum = mode
            if i == 0:
                radio_button.setChecked(True)
            radio_button.toggled.connect(self.selectAttackMode)  # Connecté à votre fonction
            self.methodGroup.addButton(radio_button, i)
            attack_layout.addWidget(radio_button, 0, i)


        # Groupe pour la sélection des fichiers et options
        options_group_box = QGroupBox("Options")
        options_layout = QGridLayout()
        options_group_box.setLayout(options_layout)
        layout.addWidget(options_group_box)

        # Fichiers d'entrée/sortie
        self.inputBtn = QPushButton("Fichier d'entrée")
        self.inputBtn.clicked.connect(self.getInputFile)
        options_layout.addWidget(self.inputBtn, 0, 0)

        self.outputBtn = QPushButton("Fichier de sortie")
        self.outputBtn.clicked.connect(self.getOutputFile)
        options_layout.addWidget(self.outputBtn, 0, 1)

        # Type de Hash
        options_layout.addWidget(QLabel("Type de Hash :"), 1, 0)
        self.hashDropdown = QComboBox()
        self.hashDropdown.addItem("Aucun", QVariant(passwordCracker.NO_HASH))
        self.hashDropdown.addItem("SHA1", QVariant(passwordCracker.SHA1))
        self.hashDropdown.addItem("MD5", QVariant(passwordCracker.MD5))
        self.hashDropdown.addItem("bcrypt", QVariant(passwordCracker.BCRYPT))
        options_layout.addWidget(self.hashDropdown, 1, 1)

        # Keyspace
        options_layout.addWidget(QLabel("Keyspace :"), 2, 0)
        self.keyspaceDropdown = QComboBox()
        resources_path = "Resources"  # Chemin vers vos fichiers de keyspace
        if os.path.exists(resources_path):
            for file in os.listdir(resources_path):
                if file.endswith(".txt"):
                    self.keyspaceDropdown.addItem(file.replace(".txt", ""),
                                                os.path.join(resources_path, file))
        options_layout.addWidget(self.keyspaceDropdown, 2, 1)

        # Longueur min/max
        options_layout.addWidget(QLabel("Min Longueur :"), 3, 0)  # Labels plus clairs
        self.minBox = QSpinBox()
        self.minBox.setRange(1, 10)
        options_layout.addWidget(self.minBox, 3, 1)

        options_layout.addWidget(QLabel("Max Longueur :"), 4, 0)
        self.maxBox = QSpinBox()
        self.maxBox.setRange(1, 10)
        options_layout.addWidget(self.maxBox, 4, 1)


        # Fichiers additionnels (dictionnaire, custom wordlist)
        self.dictionaryBtn = QPushButton("Fichier Dictionnaire")
        self.dictionaryBtn.clicked.connect(self.getDictionaryFile)
        options_layout.addWidget(self.dictionaryBtn, 5, 0)

        self.customWordlistBtn = QPushButton("Custom Wordlist")
        self.customWordlistBtn.clicked.connect(self.getCustomWordlistFile)
        options_layout.addWidget(self.customWordlistBtn, 5, 1)

        # Règles
        options_layout.addWidget(QLabel("Règles de transformation (ex: ldut) :"), 6, 0)
        self.ruleInput = QLineEdit()
        options_layout.addWidget(self.ruleInput, 6, 1)
        
        # Masques
        options_layout.addWidget(QLabel("Masque (ex: ?u?l?d):"), 7, 0)
        self.maskInput = QLineEdit()
        options_layout.addWidget(self.maskInput, 7, 1)



        # Zone de résultats
        results_group_box = QGroupBox("Résultats")
        results_layout = QVBoxLayout()
        results_group_box.setLayout(results_layout)
        layout.addWidget(results_group_box)

        self.resultText = QTextEdit()
        self.resultText.setReadOnly(True)
        results_layout.addWidget(self.resultText)


        # Bouton Démarrer
        self.startBtn = QPushButton("Démarrer l'attaque")
        self.startBtn.clicked.connect(self.startCrack)
        layout.addWidget(self.startBtn)

    def selectAttackMode(self):
        radiobutton = self.sender()
        if radiobutton.isChecked():
            self.mode = radiobutton.methodNum

    def getInputFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, 'Sélectionner un fichier d\'entrée', '', "Fichiers texte (*.txt)")
        if filePath:
            self.inputFile = filePath

    def getOutputFile(self):
        filePath, _ = QFileDialog.getSaveFileName(self, 'Enregistrer sous', '', "Fichiers texte (*.txt)")
        if filePath:
            self.outputFile = filePath

    def getDictionaryFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, 'Sélectionner un fichier dictionnaire', '', "Fichiers texte (*.txt)")
        if filePath:
            self.dictionaryFile = filePath

    def getCustomWordlistFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, 'Sélectionner un fichier custom wordlist', '', "Fichiers texte (*.txt)")
        if filePath:
            self.customWordlistFile = filePath
            
    def startCrack(self):
        keyspaceFile = self.keyspaceDropdown.currentData()
        keyspace = loadKeyspaceFromFile(keyspaceFile)

        min_length = self.minBox.value()
        max_length = self.maxBox.value()
        ruleString = self.ruleInput.text()
        maskStr = self.maskInput.text() 

        if not self.inputFile or not self.outputFile:
            self.resultText.setText("⚠️ Sélectionnez un fichier d'entrée et un fichier de sortie avant de commencer.")
            return

        cracker = passwordCracker(self.inputFile, self.outputFile)
        cracker.setHashNum(self.hashDropdown.currentData())

        self.worker = CrackingWorker(
            cracker,
            self.mode,
            keyspace,
            min_length,
            max_length,
            maskStr,
            self.dictionaryFile,
            self.customWordlistFile,
            ruleString
        )
        self.worker.update_signal.connect(self.resultText.append)
        self.worker.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec_())
    
