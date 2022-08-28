# Fibonacci series
n=int(input())
num1=0
num2=1
print(num1,num2)
for i in range(n):
    fibo=num1+num2
    num1=num2
    num2=fibo
    print(fibo)

print("The last term of the fibonacci series :",fibo)
