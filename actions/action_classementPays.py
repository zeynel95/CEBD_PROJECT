
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fonction fournie 1
class AppClassementPays(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/table_classementPays.ui", self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_classementPays, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(
                "with paysNum(pays,num) as ( SELECT distinct pays, numEq FROM LesSportifsEQ UNION SELECT pays, numSp FROM LesSportifsEQ ), \
tgoldb(pays, nb) as ( SELECT pays, COUNT(gold) FROM paysNum JOIN LesResultats ON(num = gold) GROUP BY pays ), \
tgold(pays,gold) as (SELECT DISTINCT pays, 0 FROM LesSportifsEQ WHERE pays not in (select pays from tgoldb) UNION select pays, nb FROM tgoldb), \
tsilverb(pays, nb) as ( SELECT pays, COUNT(silver) FROM paysNum JOIN LesResultats ON(num = silver) GROUP BY pays ), \
tsilver(pays,silver) as (SELECT DISTINCT pays, 0 FROM LesSportifsEQ WHERE pays not in (select pays from tsilverb) UNION select pays, nb FROM tsilverb), \
tbronzeb(pays, nb) as ( SELECT pays, COUNT(bronze) FROM paysNum JOIN LesResultats ON(num = bronze) GROUP BY pays ), \
tbronze(pays,bronze) as (SELECT DISTINCT pays, 0 FROM LesSportifsEQ WHERE pays not in (select pays from tbronzeb) UNION select pays, nb FROM tbronzeb) \
SELECT pays, gold, silver, bronze \
FROM tgold JOIN tsilver USING(pays) JOIN tbronze USING(pays) \
ORDER by gold DESC, silver DESC, bronze DESC")
        except Exception as e:
            self.ui.table_classementPays.setRowCount(0)
            display.refreshLabel(self.ui.label_classementPays, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_classementPays, result)