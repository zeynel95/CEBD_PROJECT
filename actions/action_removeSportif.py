import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

# Classe permettant d'afficher la fonction fournie 2
class AppRemoveSportif(QDialog):

    #Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/removeSportif.ui", self)
        self.data = data

    # Fonction de mise à jour de l'affichage
    def refreshResult(self):

        display.refreshLabel(self.ui.label_removeSportif, "")
        if not self.ui.lineEditSportif.text().strip() :
            display.refreshLabel(self.ui.label_removeSportif, "Veuillez remplire le champs")
        else:
            try:
                cursor = self.data.cursor()
                cursor.execute("DELETE FROM LesSportifs WHERE numSp=?;", [int(self.ui.lineEditSportif.text().strip())])
            except Exception as e:
                display.refreshLabel(self.ui.label_removeSportif, "Impossible de supprimer le Sportif : " + repr(e))
            else:
                display.refreshLabel(self.ui.label_removeSportif, ": cible elimine.")
