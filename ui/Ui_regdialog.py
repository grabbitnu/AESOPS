# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regdialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogRegister(object):
    def setupUi(self, DialogRegister):
        DialogRegister.setObjectName("DialogRegister")
        DialogRegister.resize(510, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogRegister)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelheader = QtWidgets.QLabel(DialogRegister)
        self.labelheader.setObjectName("labelheader")
        self.verticalLayout.addWidget(self.labelheader)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(DialogRegister)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.leName = QtWidgets.QLineEdit(DialogRegister)
        self.leName.setObjectName("leName")
        self.gridLayout.addWidget(self.leName, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(DialogRegister)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.leEmail = QtWidgets.QLineEdit(DialogRegister)
        self.leEmail.setObjectName("leEmail")
        self.gridLayout.addWidget(self.leEmail, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(DialogRegister)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.leWgroup = QtWidgets.QLineEdit(DialogRegister)
        self.leWgroup.setObjectName("leWgroup")
        self.gridLayout.addWidget(self.leWgroup, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(DialogRegister)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.leActCode = QtWidgets.QLineEdit(DialogRegister)
        self.leActCode.setObjectName("leActCode")
        self.gridLayout.addWidget(self.leActCode, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogRegister)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.leName)
        self.label_2.setBuddy(self.leEmail)
        self.label_4.setBuddy(self.leWgroup)
        self.label_3.setBuddy(self.leActCode)

        self.retranslateUi(DialogRegister)
        self.buttonBox.accepted.connect(DialogRegister.accept)
        self.buttonBox.rejected.connect(DialogRegister.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogRegister)

    def retranslateUi(self, DialogRegister):
        _translate = QtCore.QCoreApplication.translate
        DialogRegister.setWindowTitle(_translate("DialogRegister", "AESOPS Register"))
        self.labelheader.setText(_translate("DialogRegister", "<html><head/><body><p>You are welcome to register </p><p>as an authorized user of AESOPS\"\\u00A9\"</p></body></html>"))
        self.label.setText(_translate("DialogRegister", "Name"))
        self.label_2.setText(_translate("DialogRegister", "Email"))
        self.label_4.setText(_translate("DialogRegister", "Workgroup"))
        self.label_3.setText(_translate("DialogRegister", "Activation Code"))

