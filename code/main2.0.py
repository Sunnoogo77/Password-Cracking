# Interface graphique pour le Password Cracker adapté à ton projet

from passwordCracker import *
from CreatCharacter import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CrackingWorker(QThread):
    update_signal = pyqtSignal(str)

    def __init__(self, cracker, mode, keyspace, min_length, max_length, maskStr):
        super().__init__()
        self.cracker = cracker
        self.mode = mode
        self.keyspace = keyspace
        self.min_length = min_length
        self.max_length = max_length
        self.maskStr = maskStr

    def run(self):
        self.update_signal.emit("🔍 Starting attack...\n")

        if self.mode == Menu.BRUTE_FORCE:
            self.cracker.bruteForce(self.keyspace, self.min_length, self.max_length)
        else:
            self.cracker.maskAttack(self.maskStr)

        self.update_signal.emit(f"✅ Crack completed! Results saved in {self.cracker.outputFile}")


class Menu(QWidget):
    BRUTE_FORCE = 0
    MASK = 1

    def __init__(self):
        super().__init__()
        self.inputFile = ""
        self.outputFile = ""
        self.mode = Menu.BRUTE_FORCE
        self.methodInput = ""
        self.rules = ""
        self.appendMask = ""
        self.prependMask = ""

        self.setupUI()

    def setupUI(self):
        """Initialisation de l'interface graphique"""
        self.setGeometry(200, 20, 500, 400)
        self.setWindowTitle('Password Cracker')

        layout = QGridLayout()
        self.setLayout(layout)

        # Sélection de la méthode d'attaque
        methodGroup = QButtonGroup()
        bruteForceBtn = QRadioButton("Brute Force")
        bruteForceBtn.setChecked(True)
        bruteForceBtn.methodNum = Menu.BRUTE_FORCE
        methodGroup.addButton(bruteForceBtn, 0)
        bruteForceBtn.toggled.connect(self.selectAttackMode)
        layout.addWidget(bruteForceBtn, 0, 0)

        maskAttackBtn = QRadioButton("Masque")
        maskAttackBtn.methodNum = Menu.MASK
        methodGroup.addButton(maskAttackBtn, 1)
        maskAttackBtn.toggled.connect(self.selectAttackMode)
        layout.addWidget(maskAttackBtn, 0, 1)

        # Boutons de sélection des fichiers
        self.inputBtn = QPushButton("Sélectionner fichier d'entrée")
        self.inputBtn.clicked.connect(self.getInputFile)
        layout.addWidget(self.inputBtn, 1, 0, 1, 2)

        self.outputBtn = QPushButton("Sélectionner fichier de sortie")
        self.outputBtn.clicked.connect(self.getOutputFile)
        layout.addWidget(self.outputBtn, 2, 0, 1, 2)

        # Mode hachage
        self.hashDropdown = QComboBox(self)
        self.hashDropdown.addItem("Aucun", QVariant(passwordCracker.NO_HASH))
        self.hashDropdown.addItem("SHA1", QVariant(passwordCracker.SHA1))
        self.hashDropdown.addItem("MD5", QVariant(passwordCracker.MD5))
        self.hashDropdown.addItem("bcrypt", QVariant(passwordCracker.BCRYPT))
        layout.addWidget(self.hashDropdown, 3, 0, 1, 2)

        # Ajout des règles
        self.ruleBox = QCheckBox("Utiliser des règles")
        self.ruleBox.toggled.connect(self.toggleRules)
        layout.addWidget(self.ruleBox, 4, 0)

        # Ajout des masques
        self.maskAppendBox = QCheckBox("Append Mask")
        self.maskAppendBox.toggled.connect(self.toggleAppendMask)
        layout.addWidget(self.maskAppendBox, 4, 1)

        self.maskPrependBox = QCheckBox("Prepend Mask")
        self.maskPrependBox.toggled.connect(self.togglePrependMask)
        layout.addWidget(self.maskPrependBox, 5, 0)

        # Sélection du keyspace
        self.keyspaceLabel = QLabel("Keyspace :")
        layout.addWidget(self.keyspaceLabel, 6, 0)
        self.keyspaceBox = QComboBox(self)
        self.keyspaceBox.addItem("Lettres (a-z)", "abcdefghijklmnopqrstuvwxyz")
        self.keyspaceBox.addItem("Majuscules (A-Z)", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.keyspaceBox.addItem("Chiffres (0-9)", "0123456789")
        self.keyspaceBox.addItem("Tout (a-zA-Z0-9)", "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        layout.addWidget(self.keyspaceBox, 6, 1)

        # Min et max longueur
        self.minBoxLabel = QLabel("Min Longueur")
        layout.addWidget(self.minBoxLabel, 7, 0)
        self.minBox = QSpinBox(self)
        self.minBox.setRange(1, 10)
        layout.addWidget(self.minBox, 7, 1)

        self.maxBoxLabel = QLabel("Max Longueur")
        layout.addWidget(self.maxBoxLabel, 8, 0)
        self.maxBox = QSpinBox(self)
        self.maxBox.setRange(1, 10)
        layout.addWidget(self.maxBox, 8, 1)

        # Affichage des résultats
        self.resultText = QTextEdit(self)
        self.resultText.setReadOnly(True)
        layout.addWidget(self.resultText, 9, 0, 2, 2)

        # Bouton démarrer
        self.startBtn = QPushButton("Démarrer l'attaque", self)
        self.startBtn.clicked.connect(self.startCrack)
        layout.addWidget(self.startBtn, 11, 0, 1, 2)

    def selectAttackMode(self):
        """Sélectionner le mode d'attaque"""
        radiobutton = self.sender()
        if radiobutton.isChecked():
            self.mode = radiobutton.methodNum

    def getInputFile(self):
        """Sélectionne le fichier d'entrée"""
        filePath, _ = QFileDialog.getOpenFileName(self, 'Ouvrir un fichier', '', "Fichiers texte (*.txt)")
        if filePath:
            self.inputFile = filePath

    def getOutputFile(self):
        """Sélectionne le fichier de sortie"""
        filePath, _ = QFileDialog.getSaveFileName(self, 'Enregistrer sous', '', "Fichiers texte (*.txt)")
        if filePath:
            self.outputFile = filePath

    def toggleRules(self):
        """Enable/Disable rule file selection"""
        if self.ruleBox.isChecked():
            filePath, _ = QFileDialog.getOpenFileName(self, 'Select Rule File', '', "Text Files (*.txt)")
            if filePath:
                self.rules = filePath
        else:
            self.rules = ""

    def toggleAppendMask(self):
        """Enable/Disable append mask file selection"""
        if self.maskAppendBox.isChecked():
            filePath, _ = QFileDialog.getOpenFileName(self, 'Select Append Mask File', '', "Text Files (*.txt)")
            if filePath:
                self.appendMask = filePath
        else:
            self.appendMask = ""

    def togglePrependMask(self):
        """Enable/Disable prepend mask file selection"""
        if self.maskPrependBox.isChecked():
            filePath, _ = QFileDialog.getOpenFileName(self, 'Select Prepend Mask File', '', "Text Files (*.txt)")
            if filePath:
                self.prependMask = filePath
        else:
            self.prependMask = ""


    def startCrack(self):
        """Start password cracking in a separate thread"""
        if not self.inputFile or not self.outputFile:
            self.resultText.setText("⚠️ Select input and output files first.")
            return

        cracker = passwordCracker(self.inputFile, self.outputFile)
        cracker.setHashNum(self.hashDropdown.currentData())

        # Read rules from file
        if self.rules:
            with open(self.rules, "r", encoding="utf-8") as file:
                rulesList = file.read().splitlines()
            cracker.setRuleList(rulesList)

        # Read append/prepend masks
        if self.appendMask:
            with open(self.appendMask, "r", encoding="utf-8") as file:
                appendMaskStr = file.read().strip()
            cracker.setAppendMask(appendMaskStr)

        if self.prependMask:
            with open(self.prependMask, "r", encoding="utf-8") as file:
                prependMaskStr = file.read().strip()
            cracker.setPrependMask(prependMaskStr)

        keyspace = self.keyspaceBox.currentData()
        min_length = self.minBox.value()
        max_length = self.maxBox.value()

        maskStr = self.appendMask or self.prependMask or "?l?l?l?l"

        # Run the cracking in a separate thread
        self.worker = CrackingWorker(cracker, self.mode, keyspace, min_length, max_length, maskStr)
        self.worker.update_signal.connect(self.resultText.append)  # Update GUI
        self.worker.start()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec_())
