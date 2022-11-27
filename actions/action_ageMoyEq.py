
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fonction fournie 1
class AppAgeMoyEq(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/table_ageMoy.ui", self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_ageMoy, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(
                "WITH ageMoyEq(numEq, age) AS (SELECT numEq, cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dateNaisSp) as int) FROM LesSportifsEQ) SELECT numEq,AVG(age)  FROM ageMoyEq GROUP BY numEq HAVING numEq in (SELECT gold FROM LesResultats)")
        except Exception as e:
            self.ui.table_ageMoy.setRowCount(0)
            display.refreshLabel(self.ui.label_ageMoy, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_ageMoy, result)