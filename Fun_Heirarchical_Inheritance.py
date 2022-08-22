  # Heirarchical inheritance

class Get:
    def getin(self):
        self.a = int(input("Enter the valid number :"))
        self.b = int(input("Enter the valid number :"))

class Addition(Get):
    def add(self):
        self.getin()
        c=self.a+self.b
        print("Addition :",c)

class Subtraction(Get):
    def sub(self):
        self.getin()
        c=self.a-self.b
        print("Subtraction :",c)

 
obj1= Addition()
obj1.add()

obj2=Subtraction()
obj2.sub()
