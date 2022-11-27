
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

# Classe permettant d'afficher la fonction fournie 2
class AppInsertResult(QDialog):

    #Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/insertResult.ui", self)
        self.data = data

    # Fonction de mise à jour de l'affichage
    def refreshResult(self):

        display.refreshLabel(self.ui.label_insertResult, "")
        if not self.ui.lineEditEp.text().strip() or not self.ui.lineEditGold.text().strip() or not self.ui.lineEditSilver.text().strip() or not self.ui.lineEditBronze.text().strip():
            display.refreshLabel(self.ui.label_insertResult, "Veuillez remplire tout les champs")
        else:
            try:
                cursor = self.data.cursor()
                cursor.execute("INSERT INTO LesResultats VALUES (?,?,?,?)", [int(self.ui.lineEditEp.text().strip()), int(self.ui.lineEditGold.text().strip()), int(self.ui.lineEditSilver.text().strip()), int(self.ui.lineEditBronze.text().strip())])
            except Exception as e:
                display.refreshLabel(self.ui.label_insertResult, "Impossible d'inserer les valeur : " + repr(e))
            else:
                display.refreshLabel(self.ui.label_insertResult, "les valeurs sont inséré")
