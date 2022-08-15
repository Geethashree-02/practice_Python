class maths:
    def add(self,a,b):
        self.a=a
        self.b=b
        sum=a+b
        print(sum)

obj = maths()
a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
obj.add(a,b)
        
