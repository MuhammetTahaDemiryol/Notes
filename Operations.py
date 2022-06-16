import math

class Operations():
   
    def read_number(self,object):
        self.number=object.numberE.text()
        try:
           self.number = int(self.number)
           self.calculate_primes()
        except ValueError:
            object.statusL.setText("Enter only numerical characters")
            self.read_number()
    
    
    def calculate_primes(self):
        self.primes=[]

        for a in range(2, self.number + 1):
           # all prime numbers are greater than 1
           
           treshhold = math.floor(a/2+1)
           
           if treshhold <= 2 :
               self.primes.append(a)
           
           for divider in range (2, treshhold):
               
               if a % divider == 0:
                   break
                   # a is not a prime number
               else:
                   if divider == treshhold-1:
                       # a is a prime number
                       self.primes.append(a)
           
           
           
           
           
           
           
        print("Primes: ", self.primes)
        self.print_textbox(object)
    
    def print_textbox(self,object):
        print("Primes: ", self.primes)
        self.temp = ''
        for i in self.primes:
            self.temp=self.temp + ' ' + str(i)
        object.textEdit.setText(self.temp)
    
    def print_file(self):
        file=open('file.txt','w')
        for i in self.temp:
            file.write(str(i)+'\n')
        file.close()
        object.textEdit.setText("file.txt is in the same directory as program")
