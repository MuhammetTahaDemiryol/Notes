# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:30:23 2022

@author: Ktp2
"""

 def btnclk(self):
     col=QColor(155,255,255)
     # color.setRed(155)
     # color.setGreen(255)
     # color.setBlue(255)
     print(col.name())
     self.pushButton.setStyleSheet("background-color:yellow")
     self.label.setStyleSheet("background-color:"+col.name())
     font=QtGui.QFont()
     
     # color="color:"+self.comboBox.currentText()
     # self.label.setStyleSheet(color)
     font.setStrikeOut(bool(self.checkBox_4.checkState()))
     font.setUnderline(bool(self.checkBox_3.checkState()))
     font.setItalic(bool(self.checkBox_2.checkState()))
     font.setBold(bool(self.checkBox.checkState()))
     font.setPointSize(int(self.lineEdit.text()))
     self.label.setFont(font)
     # print(self.checkBox_2.checkState())
     */********************************************************
     working1
     ****************************************************************************************
class Employees:
    def _init_(self,firstName,lastName):
        self.__fistName=firstName
        self.__lastName=lastName
    def set_firstname(self,first):
        self.__fistName=first
    def se_lastname(self,last):
        self.__lastName=last
    def get_firstname(self):
        return self.__fistName
    def get_lastname(self):
        return self.__lastName
    def print_employee(self):
        print('name:',self.get_firstname())
        print('lastname:',self.get_lastname())
class ComissionEmployee(Employees):
    def _init_(self, firstName, lastName,com_rate,gros_sales):
        super()._init_(firstName, lastName)
        self.__com_rate=com_rate
        self.__gros_sales=gros_sales
    def set_com_rate(self,comrate):
        self.__com_rate=comrate
    def set_gros_sales(self,gros):
        self.__gros_sales=gros
    def get_com_rate(self):
        return self.__com_rate
    def get_gros_sales(self):
        return self.__gros_sales
    def print_employee(self):
        super().print_employee()
        print('commmision rate',self.get_com_rate())
        print('gross salary:',self.get_gros_sales())
    def earnings(self):
        c=BasePlusCommissionEmployee('sue', 'jones', 10000, 0.6,0)
        c.set_base_salary(0)
        e=c.get_base_salary()+(self.get_com_rate()*self.get_gros_sales())
        print(e)
class BasePlusCommissionEmployee(ComissionEmployee):
    def _init_(self, firstName, lastName, com_rate, gros_sales,base_salary):
        super()._init_(firstName, lastName, com_rate, gros_sales)
        self.__base_salary=base_salary
    def set_base_salary(self,salary):
        self.__base_salary=salary
    def get_base_salary(self):
        return self.__base_salary
    def print_employee(self):
        super().print_employee()
        print('base salary:',self.get_base_salary())
        
    def earnings(self):
        print(self.get_base_salary()+(self.get_com_rate()*self.get_gros_sales()))
        
        
def main():
    my_emp=Employees('Jonh', 'smith')
    my_emp.print_employee()
    mycomemp=ComissionEmployee('sue', 'jones', 10000, 0.6)
    mycomemp.print_employee()
    mycomemp.earnings()
    mybasecomemp=BasePlusCommissionEmployee('bob', 'lewis', 5000, 0.4, 300)
    
    mybasecomemp.print_employee()
    mybasecomemp.earnings() 
main()
   ********************************************************************************************** 
    
    working 2
    ***********************************************************************************
    self.lineEdit.textChanged.connect(self.linechange)
    self.comboBox.activated[str].connect(self.combochange)
    # self.pushButton.clicked.connect(self.print_textbox)
    # self.pushButton.clicked.connect(self.write_file)
    self.pushButton.clicked.connect(self.prime)
    self.pushButton.clicked.connect(self.runclick)
    self.lineEdit.textChanged.connect(self.change)
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
    
    

def change(self,text):
    self.color=text
    print(self.color)
def write_file(self,lst):
    # lst=self.prime()
    filew=open('file.txt','w')
    for i in lst:
        filew.write(str(i)+'\n')
    filew.close()
    self.textEdit.setText('')
def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.comboBox.setItemText(0, _translate("MainWindow", "print the text box"))
    self.pushButton.setText(_translate("MainWindow", "run"))
    self.label.setText(_translate("MainWindow", "enter number"))
    self.label_2.setText(_translate("MainWindow", "status"))
    
*****************************************************************************    
calculator 
***************************************************************************    
    
class Real:
    
    def __init__(self,n1,n2):
        self.__num1 = n1
        self.__num2 = n2
        
    def set_num1(self,n1):
        self.__num1 = n1
        
    def set_num2(self,n2):
        self.__num2 = n2
        
    def get_num1(self):
        return self.__num1
        
    def get_num2(self):
        return self.__num2
        
    def add(self):
        return self.__num1+self.__num2
    
    def substract(self):
        return self.__num1-self.__num2
   
    
class Complex(Real):
    
    def __init__(self,r1,i1,r2,i2):
        
        Real.__init__(self,r1,r2)
        
        self.__imag1 = i1
        self.__imag2 = i2
    
    
    def set_imag1(self,i1):
        self.__imag1 = i1
        
    def set_imag2(self,i2):
        self.__imag1 = i2
        
    def get_imag1(self):
        return self.__imag1
        
    def get_imag2(self):
        return self.__imag2
        
    def add(self):
        return self.get_num1()+self.get_num2(), self.__imag1+self.__imag2
    
    def substract(self):
        return self._Real__num1-self._Real__num2,self.__imag1-self.__imag2
    
    *******************************************************************************************
    input dialog
    ***********************************************************************************
    def showDialog(self):
        text,ok=QInputdialog.getText(self,'Input Dialog','enter your name')
        if ok:
            self.lineedit.setText(str(text))
***********************************************************************
    sender
***********************************************************************
sender =self.sender()
self.statusBar().showMessage(sender.text()+'was pressed')
    