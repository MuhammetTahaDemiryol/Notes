# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:50:13 2022

@author: Taha
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QPushButton, QMessageBox, QDesktopWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(53, 90, 331, 71))
        self.textEdit.setObjectName("textEdit")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 230, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 270, 191, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("write to file")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(46, 230, 121, 20))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(56, 320, 111, 20))
        self.label_2.setObjectName("label_2")
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.lineEdit.textChanged.connect(self.linechange)
        self.comboBox.activated[str].connect(self.combochange)
        # self.pushButton.clicked.connect(self.print_textbox)
        # self.pushButton.clicked.connect(self.write_file)
        self.pushButton.clicked.connect(self.prime)
        self.pushButton.clicked.connect(self.runclick)
        self.retranslateUi(MainWindow)
        print(self.comboBox.currentText())
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        
    def runclick(self):
        if self.comboBox.currentText()=='print the text box':
            lst=self.prime()
            self.print_textbox(lst)
        else:
            lst=self.prime()
            self.write_file(lst)
    
    def combochange(self):
        self.label_2.setText(self.comboBox.currentText())
        
    def linechange(self):
        no_error=self.lineEdit.text().isdigit()
        if no_error:
            self.label_2.setText('normal')
        else:
            self.label_2.setText('error')
    def print_textbox(self,lst2):
        # lst2=self.prime()
        strliste=""
        for i in lst2:
            strliste=strliste + ' ' + str(i)
        self.textEdit.setText(strliste)
        
    def prime(self):
        primes=[]
        num=int(self.lineEdit.text())
        for num in range(0, num+1):
           # all prime numbers are greater than 1
           if num > 1:
               for i in range(2, num):
                   if (num % i) == 0:
                       break
               else:
                 primes.append(num)
        return primes
    
        
    def write_file(self,lst):
        # lst=self.prime()
        filew=open('file.txt','w')
        for i in lst:
            filew.write(str(i)+'  ')
        filew.close()
        self.textEdit.setText('')
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "print the text box"))
        self.pushButton.setText(_translate("MainWindow", "run"))
        self.label.setText(_translate("MainWindow", "enter number"))
        self.label_2.setText(_translate("MainWindow", "status"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())