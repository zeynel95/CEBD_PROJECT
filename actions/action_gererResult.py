
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

# Classe permettant d'afficher la fonction fournie 2
class AppGereResultat(QDialog):

    #Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/gererResultat.ui", self)
        self.data = data

    def removeResultat(self):

        display.refreshLabel(self.ui.label_supprimeResultat, "")
        if not self.ui.lineEditRemoveEp.text().strip():
            display.refreshLabel(self.ui.label_supprimeResultat, "Veuillez remplire le champs")
        else:
            try:
                cursor = self.data.cursor()
                cursor.execute("DELETE FROM LesResultats WHERE numEp=?;", [int(self.ui.lineEditRemoveEp.text().strip())])
            except Exception as e:
                display.refreshLabel(self.ui.label_supprimeResultat, "Impossible de supprimer le  : " + repr(e))
            else:
                display.refreshLabel(self.ui.label_supprimeResultat, ": cible elimine.")

    # Fonction de mise à jour de l'affichage
    def insertResultat(self):

        display.refreshLabel(self.ui.label_insertResultat, "")
        if not self.ui.lineEditEp.text().strip() or not self.ui.lineEditGold.text().strip() \
            or not self.ui.lineEditSilver.text().strip() or not self.ui.lineEditBronxe.text().strip():
            display.refreshLabel(self.ui.label_insertResultat, "Veuillez remplire tout les champs")
        else:
            try:
                cursor = self.data.cursor()
                cursor.execute("INSERT INTO LesResultats VALUES (?,?,?,?)", [int(self.ui.lineEditEp.text().strip()),
                 int(self.ui.lineEditGold.text().strip()), int(self.ui.lineEditSilver.text().strip()), int(self.ui.lineEditBronxe.text().strip())])
                self.data.commit()
            except Exception as e:
                display.refreshLabel(self.ui.label_insertResultat, "Impossible d'inserer les valeur : " + repr(e))
            else:
                display.refreshLabel(self.ui.label_insertResultat, "les valeurs sont inséré")

    def modifResultat(self):

        display.refreshLabel(self.ui.label_modifResultat, "")
        if not self.ui.lineEditModifIn.text().strip() or \
            not self.ui.lineEditModifResGold.text().strip() or \
            not self.ui.lineEditModifResSilver.text().strip() or not self.ui.lineEditModifResBronxe.text().strip():
            display.refreshLabel(self.ui.label_modifResultat, "Veuillez remplire tout les champs")
        else:
            try:
                cursor = self.data.cursor()
                cursor.execute('''UPDATE LesResultats
                                    SET gold=?, silver=?, bronze=?
                                    WHERE numEp = ?;''', [
                                        int(self.ui.lineEditModifResGold.text().strip()), int(self.ui.lineEditModifResSilver.text().strip()),
                                        int(self.ui.lineEditModifResBronxe.text().strip()),
                                        int(self.ui.lineEditModifIn.text().strip()), 
                                    ])
                                    
            except Exception as e:
                display.refreshLabel(self.ui.label_modifResultat, "Impossible d'inserer les valeur : " + repr(e))
            else:
                display.refreshLabel(self.ui.label_modifResultat, "les valeurs sont modifie")            