# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# __author__ = 'Zhenyu Zhang'

from PyQt5.QtWidgets import QDialog

from .Ui_regdialog import Ui_DialogRegister


class DialogRegister(QDialog, Ui_DialogRegister):
    def __init__(self, parent=None):
        super(DialogRegister, self).__init__(parent)
        self.setupUi(self)
        self.labelheader.setText(
            "<b><font color=\"black\" size=\"4\">" +
            "You are welcome to register\n as an authorized user of AESOPS" +
            "\u00A9" + " </font>" + "</b>")
        return
