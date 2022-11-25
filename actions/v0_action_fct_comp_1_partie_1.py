import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic


# Classe permettant d'afficher la fonction à compléter 3
class AppFctComp1Partie1(QDialog):

    # Constructeur
    def __init__(self, data: sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_comp_1_modofie.ui", self)
        self.data = data
        # ici on affiche tout les categorie dans la table 
        cursor = self.data.cursor()
        temp = cursor.execute("SELECT DISTINCT categorieEp FROM V0_LesEpreuves")
        display.refreshGenericData(self.ui.tableWidget, temp)
        

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):
        # TODO 1.1 : fonction à modifier pour remplacer la zone de saisie par une liste de valeurs prédéfinies
        #  dans l'interface une fois le fichier ui correspondant mis à jour
        #ici on recupere le nom de la categorie selectionne
        if not self.ui.tableWidget.currentItem():
            self.ui.table_fct_comp_1.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_1, "Veuillez indiquer un nom de catégorie")
        else:
            try:
                cursor = self.data.cursor()
                result = cursor.execute(
                    "SELECT numEp, nomEp, formeEp, nomDi, categorieEp, nbSportifsEp, strftime('%Y-%m-%d',dateEp,'unixepoch') FROM V0_LesEpreuves WHERE categorieEp = ?",
                    [self.ui.tableWidget.currentItem().text()])
            except Exception as e:
                self.ui.table_fct_comp_1.setRowCount(0)
                display.refreshLabel(self.ui.label_fct_comp_1, "Impossible d'afficher les résultats : " + repr(e))
            else:
                i = display.refreshGenericData(self.ui.table_fct_comp_1, result)
                if i == 0:
                    display.refreshLabel(self.ui.label_fct_comp_1, "Aucun résultat")
