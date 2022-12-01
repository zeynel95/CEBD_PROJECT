
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

# Classe permettant d'afficher la fonction fournie 2
class AppGereEpreuve(QDialog):

    #Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/gererInscription.ui", self)
        self.data = data

    def removeInscription(self):


        display.refreshLabel(self.ui.label_removeEp, "")
        if not self.ui.lineEditRemoveEp.text().strip() or not self.ui.lineEditRemoveIn.text().strip():
            display.refreshLabel(self.ui.label_removeEp, "Veuillez remplire le champs")
        else:
            try:
                cursor = self.data.cursor()
                cursor.execute("DELETE FROM LesInscriptions WHERE numEp=? and numIn=?;", [int(self.ui.lineEditRemoveEp.text().strip()), int(self.ui.lineEditRemoveIn.text().strip())])
            except Exception as e:
                display.refreshLabel(self.ui.label_removeEp, "Impossible de supprimer le  : " + repr(e))
            else:
                display.refreshLabel(self.ui.label_removeEp, ": cible elimine.")

    # Fonction de mise à jour de l'affichage
    def insertInscription(self):

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

    def ModifInscription(self):

        display.refreshLabel(self.ui.label_insertEpreuve_2, "")
        if not self.ui.lineEditModifIn.text().strip() or not self.ui.lineEditModifEpAnc.text().strip() or not self.ui.lineEditModifEpNou.text().strip():
            display.refreshLabel(self.ui.label_insertEpreuve_2, "Veuillez remplire tout les champs")
        else:
            try:
                cursor = self.data.cursor()
                cursor.execute('''UPDATE LesInscriptions
                                    SET numEp=?
                                    WHERE numEp = ? and numIn=?;''', [int(self.ui.lineEditModifEpNou.text().strip()), 
                                    int(self.ui.lineEditModifEpAnc.text().strip()), int(self.ui.lineEditModifIn.text().strip())])
            except Exception as e:
                display.refreshLabel(self.ui.label_insertEpreuve_2, "Impossible d'inserer les valeur : " + repr(e))
            else:
                display.refreshLabel(self.ui.label_insertEpreuve_2, "les valeurs sont inséré")            