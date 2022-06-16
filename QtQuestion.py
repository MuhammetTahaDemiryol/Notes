# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from Operations import Operations 

class Form(object):
    def __init__(self):
        self.op = Operations()
  
    def setupUi(self, MainWindow):
        
        
        MainWindow.setObjectName("Form")
        MainWindow.resize(361, 364)
        MainWindow.setMinimumSize(QtCore.QSize(361, 364))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.textEdit)
        
        self.numberL = QtWidgets.QLabel(self.centralwidget)
        self.numberL.setObjectName("numberL")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numberL)
        
        self.numberE = QtWidgets.QLineEdit(self.centralwidget)
        self.numberE.setMinimumSize(QtCore.QSize(151, 21))
        self.numberE.setObjectName("numberE")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.numberE)
        
        
        #Horizontal Layout
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.cB = QtWidgets.QComboBox(self.centralwidget)
        self.cB.setMinimumSize(QtCore.QSize(151, 31))
        self.cB.setObjectName("cB")
        self.cB.addItem("")
        self.cB.addItem("")
        self.horizontalLayout.addWidget(self.cB)
        
        self.pB = QtWidgets.QPushButton(self.centralwidget)
        self.pB.setMinimumSize(QtCore.QSize(93, 28))
        self.pB.setMaximumSize(QtCore.QSize(93, 28))
        self.pB.setObjectName("pB")
        self.horizontalLayout.addWidget(self.pB)
        
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        
        
        self.statusL = QtWidgets.QLabel(self.centralwidget)
        self.statusL.setObjectName("statusL")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.statusL)
        MainWindow.setCentralWidget(self.centralwidget)
       
       

        self.retranslateUi(MainWindow)
        self.cB.currentTextChanged['QString'].connect(self.statusL.setText)
        self.pB.clicked.connect(lambda : self.op.read_number(self))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.numberL.setText(_translate("MainWindow", "Enter Number"))
        self.cB.setItemText(0, _translate("MainWindow", "Print the text box"))
        self.cB.setItemText(1, _translate("MainWindow", "Write the file"))
        self.pB.setText(_translate("MainWindow", "RUN"))
        self.statusL.setText(_translate("MainWindow", "Print the text box"))


