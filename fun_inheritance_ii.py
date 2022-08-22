  #  MULTIPLE INHERITANCE(Method_ii)

class Addition:
    def add(self):
        a=int(input("Enter the value for a :"))
        b=int(input("Enter the value for b :"))
        self.a = a
        self.b = b
        c = a+b
        print("Addition :",c)

class Subtraction:
    def sub(self):
        c = self.a-self.b
        print("Subtraction :",c)

class Multiplication(Addition,Subtraction):
    def multi(self):
        self.add()
        self.sub()
        c=self.a*self.b
        print("Multiplication :",c)

obj=Multiplication()
#obj.add()
#obj.sub()
obj.multi()
