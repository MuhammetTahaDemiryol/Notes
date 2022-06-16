# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:36:28 2022

@author: Taha
"""

from PyQt5 import  QtWidgets

import QtQuestion as Q

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Q.Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())