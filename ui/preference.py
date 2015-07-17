# -*- coding: utf-8 -*-

"""
Module implementing DialogPreference.
"""

from PyQt5.QtCore import pyqtSlot, QStringListModel
from PyQt5.QtWidgets import QDialog

from .Ui_preference import Ui_DialogPreference
from common.arith import Arith

class DialogPreference(QDialog, Ui_DialogPreference):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None,arith=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(DialogPreference, self).__init__(parent)
        self.setupUi(self)
        if arith:
            self.arith=arith
            self.setArith(arith)
        else:
            self.arith=Arith()
        # self.modes=['+-','+-*/']
            self.params=[]
    def setArith(self,arith):
        self.arith=arith
        self.modeModel = QStringListModel(self.arith.modeTexts[self.arith.diffiLevel])
        self.cmbTestModes.setModel(self.modeModel)
        self.diffiModel = QStringListModel(self.arith.difficulties)
        self.cmbDifficulty.setModel(self.diffiModel)
        self.showArith()
        self.setParameters(arith)
        return

    def setParameters(self,arith):
        self.params=[
            arith.digit,
            arith.getnTest(),
            arith.nOperands,
            arith.nDataColumn,
            arith.mode,
            arith.timerOn
        ]
        return

    def showArith(self):
        # print(self.arith.digit)
        self.leDigits.setText(str(self.arith.digit))
        self.leTestNum.setText(str(self.arith.getnTest()))
        self.leNOperands.setText(str(self.arith.nOperands))
        self.leNDataColumn.setText(str(self.arith.nDataColumn))
        self.cmbTestModes.setCurrentIndex(self.arith.mode)
        self.cmbDifficulty.setCurrentIndex(self.arith.diffiLevel)
        self.rbtnTimer.setChecked(self.arith.timerOn)
        return

    @pyqtSlot()
    def on_btnApply_clicked(self):
        """
        Slot documentation goes here.
        """
        self.arith.digit=int(self.leDigits.text())
        self.arith.setnTest(int(self.leTestNum.text()))
        self.arith.nOperands=int(self.leNOperands.text())
        self.arith.nDataColumn=int(self.leNDataColumn.text())
        self.arith.mode=self.cmbTestModes.currentIndex()
        self.arith.timerOn=self.rbtnTimer.isChecked()
        self.setParameters(self.arith)
        return

    @pyqtSlot()
    def on_buttonBox_accepted(self):
        """
        Slot documentation goes here.
        """
        self.on_btnApply_clicked()
        # print('accept')
        return
        
    @pyqtSlot()
    def on_buttonBox_rejected(self):
        """
        Slot documentation goes here.
        """
        return
