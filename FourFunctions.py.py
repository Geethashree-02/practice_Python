class maths:
    
 # with args without return
     def sub(self,a,b):
         self.a=a
         self.b=b
         minus = a-b
         print("Subtraction is ",minus)
#without args without return
     def multi(self):
         multiple = self.a*self.b
         print("Multiplication is ",multiple)

#with args with return
     def add(self,a,b):
         sum = a+b
         return (sum)

#without args with return
     def div(self):
         division = self.a/self.b
         return division
        

obj = maths()
obj.sub(5,2)
obj.multi()
Mul= obj.add(5,2)
print("Addition is ",Mul)
Div = obj.div()
print("Division is ",Div)
