
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

# Classe permettant d'afficher la fonction fournie 2
class AppInsertEpreuve(QDialog):

    #Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/insertEpreuve.ui", self)
        self.data = data

    # Fonction de mise à jour de l'affichage
    def refreshResult(self):

        display.refreshLabel(self.ui.label_insertEpreuve, "")
        if not self.ui.lineEditNum.text().strip() or not self.ui.lineEditEp.text().strip():
            display.refreshLabel(self.ui.label_insertEpreuve, "Veuillez remplire tout les champs")
        else:
            try:
                cursor = self.data.cursor()
                cursor.execute("INSERT INTO LesInscriptions VALUES (?,?)", [int(self.ui.lineEditEp.text().strip()), int(self.ui.lineEditNum.text().strip())])
            except Exception as e:
                display.refreshLabel(self.ui.label_insertEpreuve, "Impossible d'inserer les valeur : " + repr(e))
            else:
                display.refreshLabel(self.ui.label_insertEpreuve, "les valeurs sont inséré")
