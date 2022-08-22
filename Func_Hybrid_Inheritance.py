# Hybrid Inheritance

class Get:
    def getin(self):
        self.a = int(input("Enter the values for a :"))
        self.b = int(input("Enter the values for b :"))

class Addition(Get):
    def add(self):
        self.getin()
        c = self.a+self.b
        print("Addition :",c)

class Subtraction(Get):
    def sub(self):
        self.getin()
        c = self.a-self.b
        print("Subtraction :",c)

class Arithmetic(Addition,Subtraction):
    def arith(self):
        self.add()
        self.sub()

obj = Arithmetic()
obj.arith()
