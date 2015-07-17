# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import sys, os
#import time
# tool_paths=['/./ui',
#     '/./common']
# for _path in tool_paths:
#     modulepath = os.path.dirname(os.path.realpath(__file__)) + _path
#     print(modulepath)
#     sys.path.append(modulepath)

from math import *
import time
from ui.mainwindow import MainWindow
from common.rngint import RandomInteger
from common.arith import Arith
# import aesops_rc

def main():
    from PyQt5.QtWidgets import QApplication
    # from PyQt5.QtWidgets import QSplashScreen
    # from PyQt5.QtGui import QPixmap
    # from PyQt5.QtCore import Qt
    app=QApplication.instance()
    if not app:
        app=QApplication(sys.argv)

    # splash_pix = QPixmap('://rc/pic/Aesop.png')
    # splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    # splash.setMask(splash_pix.mask())
    # splash.show()
#    splash.showMessage("Loaded modules")

    # app.processEvents()
    # Simulate something that takes time
    # time.sleep(3)
    # splash.hide()
    # splash.close()

    arith=Arith()

    mainwindow = MainWindow()
    mainwindow.setArith(arith)
    mainwindow.show()

    # mainwindow.actionQuit.triggered.connect(self.quit())
    # mainwindow.close.
    # splash.finish(mainwindow)

    sys.exit(app.exec_())

# def quit(app):
#     QAppplic
if __name__=="__main__":
    main()
