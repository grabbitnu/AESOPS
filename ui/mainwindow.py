# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from math import *
import numpy as np
import sys,csv


from PyQt5.QtCore import pyqtSlot,QCoreApplication, QTimer,Qt,QTime, QStringListModel
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem,QSizePolicy,QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QFileDialog,QDialog,QHeaderView
from PyQt5.QtGui import QIntValidator, QColor

from .Ui_mainwindow import Ui_MainWindow
from common.arith import Arith
from common.numstringparser import NumericStringParser
from ui.preference import DialogPreference

__arith_title__= \
"AESOPS\n" \
"Arithmetic Educator for Study Of Primary Students\n\n" \
"by Zhenyu Zhang\n" \
"Copyright 2014-2018\n\n" \
"contact: zyzhang@nuaa.edu.cn\n"

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.arith=None
        self.preference=DialogPreference()
        self.timer=QTimer()
        self.timer.setInterval(10)
        self.caseIsOpen=False
        self.labelTotalMark.setText("")
        self.labelTime.setText("")
        self.createConnections()
        self.qtime=QTime()
        self.timeStart=0
        self.timeElapsed=0

    def createConnections(self):
        # self.actionNew_Test.triggered.connect(self.on_btnNew_clicked)
        # self.actionSave.triggered.connect(self.on_actionSave_triggered)
        # self.btnSave.clicked.connect(self.on_btnSave_clicked)
        self.tableTestpaper.itemChanged.connect(self.on_tableTestPaper_itemChanged)
        self.cmbDifficulty.currentIndexChanged.connect(self.on_cmbDifficulty_currentIndexChanged)
        self.cmbMode.currentIndexChanged.connect(self.on_cmbMode_currentIndexChanged)
        return

    def setArith(self,arith):
        self.arith=arith
        self.answers=np.zeros(arith.getnTest())+self.arith.smallest

        self.setDifficulty()
        self.setMode()

        if not (arith.timerOn):
            self.labelTimeName.hide()
            self.labelTime.hide()

        self.preference.setArith(arith)
        return

    def setMode(self):
        self.modeModel = QStringListModel(self.arith.modeTexts[self.arith.diffiLevel])
        self.cmbMode.setModel(self.modeModel)
        self.cmbMode.setCurrentIndex(self.arith.mode)
        return
    def setDifficulty(self):
        # diffi=QListWidgetItem()
        # diffi.setText(self.arith.difficulties)
        # self.cmbDifficulty.setModel(diffi)
        self.diffiModel=QStringListModel(self.arith.difficulties)
        self.cmbDifficulty.setModel(self.diffiModel)
        self.cmbDifficulty.setCurrentIndex(self.arith.diffiLevel)
        return

    def on_cmbMode_currentIndexChanged(self):
        self.arith.mode=self.cmbMode.currentIndex()
        # self.cmbMode.setCurrentIndex(self.arith.mode)
        return
    def on_cmbDifficulty_currentIndexChanged(self):
        self.arith.diffiLevel=self.cmbDifficulty.currentIndex()
        self.cmbDifficulty.setCurrentIndex(self.arith.diffiLevel)

        self.modeModel = QStringListModel(self.arith.modeTexts[self.arith.diffiLevel])
        self.cmbMode.setModel(self.modeModel)
        if self.arith.mode>=len(self.arith.modeTexts[self.arith.diffiLevel]):
            self.arith.mode=0
        self.cmbMode.setCurrentIndex(self.arith.mode)
        return

    @pyqtSlot()
    def on_tableTestPaper_itemChanged(self):
        self.caseIsOpen=True
        return
    @pyqtSlot()
    def on_btnNew_clicked(self):
        """
        Slot documentation goes here.
        """
        self.arith.new()
        self.resetWidgets()
        return

    def resetWidgets(self):
        self.newTestTable()
        self.updateWindow()
        self.caseIsOpen=True

        if self.arith.timerOn:
            # self.timer.start()
            self.qtime.restart()
        return
    def newTestTable(self):
        self.tableTestpaper.clear()

        ncolumn=3*self.arith.nDataColumn
        self.tableTestpaper.setColumnCount(ncolumn)
        nTest=self.arith.getnTest()
        nrow=ceil(nTest/self.arith.nDataColumn)
        self.tableTestpaper.setRowCount(nrow)
        self.tableTestpaper.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        headerLabels=[]
        for i in range(0,self.arith.nDataColumn):
            labels=['Expression', 'Answer','Y/N']
            headerLabels+=labels
        self.tableTestpaper.setHorizontalHeaderLabels(headerLabels)
        self.tableTestpaper.resizeColumnsToContents()
        self.tableTestpaper.horizontalHeader().setStretchLastSection(True)
        self.tableTestpaper.horizontalHeader().resizeSections(QHeaderView.Stretch)

        for k in range(0,3,2):
            icol=0
            for j in range(0,self.arith.nDataColumn):
                irow=0
                for i in range(j,nTest,int(ncolumn/3)):
                    item=QTableWidgetItem()
                    flags=Qt.ItemIsSelectable | Qt.ItemIsEnabled
                    item.setFlags(flags)
                    self.tableTestpaper.setItem(irow,icol+k,item)
                    irow+=1
                icol+=3
        k=1
        icol=0
        for j in range(0,self.arith.nDataColumn):
            irow=0
            for i in range(j,nTest,int(ncolumn/3)):
                # item = QLineEdit()
                # item.setValidator(QIntValidator(item))
                # self.tableTestpaper.setCellWidget(irow, icol+k, item)
                item=QTableWidgetItem()
                flags=Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled
                item.setFlags(flags)
                self.tableTestpaper.setItem(irow,icol+k,item)
                irow+=1
            icol+=3
        return

    def updateTestPaper(self):
        ncolumn=3*self.arith.nDataColumn
        nTest=self.arith.getnTest()
        icol=0
        for j in range(0,self.arith.nDataColumn):
            irow=0
            for i in range(j,nTest,int(ncolumn/3)):
                self.tableTestpaper.item(irow,icol).setText(self.arith.texts[i])
                irow+=1
            icol+=3
        return

    def updateWindow(self):
        self.updateTestPaper()
        self.updateResultWindow()

        self.cmbDifficulty.setCurrentIndex(self.arith.diffiLevel)
        self.cmbMode.setCurrentIndex(self.arith.mode)
        return

    def updateResultWindow(self):
        # TODO:
        return

    def getAnswers(self):
        """
        read answer from self.tableTestPaper
        """
        ncolumn=3*self.arith.nDataColumn
        nTest=self.arith.getnTest()
        nrow=ceil(nTest/self.arith.nDataColumn)

        nsp=NumericStringParser()
        ok=False
        icol=1
        for j in range(0,self.arith.nDataColumn):
            irow=0
            for i in range(j,nTest,int(ncolumn/3)):
                text=self.tableTestpaper.item(irow,icol).text()
                # text=self.tableTestpaper.cellWidget(irow,icol).text()
                if not (text.strip()==str('')):
                    itext=int(text.strip(),10)
                    self.answers[i]=int(text.strip(),10)
                # goodanswers=nsp.eval(self.tableTestpaper.item(irow,icol-1).text())
                # print("%d, %d: %d, %d\n" % (irow,icol,self.answers[i], goodanswers))
                irow+=1
            icol+=3
        return

    def outputMarkReport(self):
        self.totalMarks=self.arith.getTotalMark()
        self.marks=self.arith.getMarks()
        self.labelTotalMark.setText(str(self.totalMarks))

        ncolumn=3*self.arith.nDataColumn
        nTest=self.arith.getnTest()
        nrow=ceil(nTest/self.arith.nDataColumn)

        icol=2
        for j in range(0,self.arith.nDataColumn):
            irow=0
            for i in range(j,nTest,int(ncolumn/3)):
                text=self.tableTestpaper.item(irow,icol-1).text()
                if (text.strip()==str('')):
                    mark='?'
                    color=Qt.gray
                elif self.marks[i]==1:
                    mark='Y' #'√'
                    color=Qt.green
                elif self.marks[i]==0:
                    mark='X'
                    color=Qt.red

                # item=self.tableTestpaper.item(0,0).s
                # self.tableTestpaper.item(irow,icol).setBackgroundColor(color)
                # self.tableTestpaper.item(irow,icol).setBackground(QColor(100,100,150))
                self.tableTestpaper.item(irow,icol).setBackground(color)
                self.tableTestpaper.item(irow,icol).setText(mark)
                # self.tableTestpaper.item(irow,icol).setWidth(80)

                irow+=1
            icol+=3

        if self.arith.timerOn:
            self.labelTimeName.show()
            self.labelTime.show()
            self.labelTime.setText(str(self.timeElapsed)+' sec')
        return

    def openFile(self):
        fname,  _ = (QFileDialog.getOpenFileName(self, \
            "Open File", "./", \
            "CSV File (*.csv);;Text file (*.txt);;All Files (*)"))
        if not fname:
            # QMessageBox.information(self, "Unable to open file",
            #         "There was an error opening \"%s\"" % fname)
            return
        with open(fname, 'rt',encoding='utf8') as stream:
            reader = csv.reader(stream,delimiter=',')
            i=0
            for row in reader:
                if (i==1):
                    self.arith.diffiLevel=int(row[1])
                    self.arith.mode=int(row[3])
                if (i==2):
                    ncol=len(row)
                    self.arith.nDataColumn=int(ncol/3)
                    # print(self.arith.nDataColumn)
                i+=1
            nrowfile=i
            nrow=i-2
            # print(nrow)
            # self.tableTestpaper.setRowCount(nrow)
            # self.tableTestpaper.setColumnCount(ncol)
            stream.seek(0)
            i=0
            for row in reader:
                if (i==nrowfile-1):
                    ncol=int(len(row)/3)
                    # print(ncol)
                    self.arith.nTest=(nrow-1)*self.arith.nDataColumn+ncol
                    # self.arith.nDataColumn=int(ncol/3)
                    # print(self.arith.nDataColumn)
                i+=1


            self.arith.new()
            # print(self.arith.nTest)
            # print(self.arith.nDataColumn)
            # print()
            # self.newTestTable()
            # self.on_btnNew_clicked()
            irow=0
            i=0
            stream.seek(0)
            for row in reader:
                if (irow>=2):
                    # print(irow)
                    if irow<nrowfile-1:
                        ncol1=self.arith.nDataColumn
                    else:
                        ncol1=int(len(row)/3)
                    icol=0
                    for j in range(icol,len(row),3):
                        text=row[j]
                        # item=self.tableTestpaper.item(irow-2,j)
                        # if not item:
                        #     item=QTableWidgetItem()
                        #     flags=Qt.ItemIsSelectable | Qt.ItemIsEnabled
                        #     item.setFlags(flags)
                        #     self.tableTestpaper.setItem(irow-2,j,item)
                        # self.tableTestpaper.item(irow-2,j).setText(text)
                        self.arith.texts[i]=text
                        # print(irow,j,self.arith.texts[i])
                        i+=1
                irow+=1
            self.arith.calcResults()
            self.resetWidgets()
            # self.caseIsOpen=True
        # self.arith.empty=False
        return
    def saveFile(self):
        fname,  _ = (QFileDialog.getSaveFileName(self, \
            "Save File As", "./", \
            "CSV File (*.csv);;Text file (*.txt);;All Files (*)")) #???
        # print(fname)
        if not fname:
            # QMessageBox.information(self, "Unable to open file",
            #         "There was an error opening \"%s\"" % fname)
            return
        with open((fname), 'wt',encoding='utf8') as stream:
            writer = csv.writer(stream)
            writer.writerow(['Marks:', str(self.totalMarks), 'Elapsed time(sec): ', str(self.timeElapsed)])
            writer.writerow(['Difficulty: ',self.arith.diffiLevel,'Mode: ', self.arith.mode])
            for row in range(0,self.tableTestpaper.rowCount()):
                rowdata = []
                for column in range(self.tableTestpaper.columnCount()):
                    item = self.tableTestpaper.item(row, column)
                    # item is not None or
                    if item.text() is not str(''):
                        rowdata.append(
                            (item.text()))#.encode('utf8'))
                    else:
                        rowdata.append(str('N/A'))
                writer.writerow(rowdata)
        # try:
        #     f = open(fname, 'w')
        # except IOError:
        #     QtGui.QMessageBox.information(self, "Unable to write file",
        #             "There was an error when writing to \"%s\"" % fname)
        #     return
        # self.arith.saveToHandle(f)
        # f.close()
        self.caseIsOpen=False
        return
    @pyqtSlot()
    def on_btnReset_clicked(self):
        """
        Slot documentation goes here.
        """
        self.arith.reset()
        self.updateWindow()
        return

    @pyqtSlot()
    def on_btnSave_clicked(self):
        """
        Slot documentation goes here.
        """
        if not self.arith.empty:
            self.saveFile()
        else:
            QMessageBox.information(self, "Unable to save file",
                    "The test paper is still empty" )
        return

    @pyqtSlot()
    def on_btnMark_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.arith.timerOn:
            # self.timer.stop()
            self.timeElapsed=float(self.qtime.elapsed())/1000.0
        self.getAnswers()
        self.arith.mark(self.answers)
        self.outputMarkReport()
        return

    @pyqtSlot()
    def on_btnStop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.timer.stop()
        return

    @pyqtSlot()
    def on_btnQuit_clicked(self):
        """
        Slot documentation goes here.
        """
        if(self.caseIsOpen==False):
            QCoreApplication.instance().quit()
        else:
            reply = QMessageBox.question(self, 'Warning',
                "Test not saved. Are you sure to quit?", QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                QCoreApplication.instance().quit()
            # else:
            #     event.ignore()
        return

    @pyqtSlot()
    def on_btnOpen_clicked(self):
        """
        Slot documentation goes here.
        """
        self.openFile()
        return

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        """
        Slot documentation goes here.
        """
        self.openFile()
        return

    @pyqtSlot()
    def on_actionSave_triggered(self):
        """
        Slot documentation goes here.
        """
        if not self.arith.empty:
            self.saveFile()
        else:
            QMessageBox.information(self, "Unable to save file",
                    "The test paper is still empty" )
        return

    @pyqtSlot()
    def on_actionPreferences_triggered(self):
        """
        Slot documentation goes here.
        """
        self.preference.setArith(self.arith)
        if(self.preference.exec_()==QDialog.Accepted):
            self.arith.digit, self.arith.nTest, \
            self.arith.NOperands, self.arith.nDataColumn, \
            self.arith.mode, self.arith.timeOn=tuple(self.preference.params)

        self.answers=np.zeros(self.arith.getnTest())+self.arith.smallest
        if not self.arith.timerOn:
            self.labelTimeName.hide()
            self.labelTime.hide()
        else:
            self.labelTimeName.show()
        return

    @pyqtSlot()
    def on_actionAbout_triggered(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.information(self, "About Arith",
                    __arith_title__)
        return

    @pyqtSlot()
    def on_actionNew_Test_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.on_btnNew_clicked()
        return

    @pyqtSlot()
    def on_actionQuit_triggered(self):
        """
        Slot documentation goes here.
        """
        QCoreApplication.instance().quit()
        return

    @pyqtSlot()
    def on_actionReset_triggered(self):
        """
        Slot documentation goes here.
        """
        self.arith.reset()
        self.updateWindow()
        return

    @pyqtSlot()
    def on_actionMark_triggered(self):
        """
        Slot documentation goes here.
        """
        self.on_btnMark_clicked()
        return

def main():
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
