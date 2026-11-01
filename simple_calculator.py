print("*****Simple Calculator*****")
print("addition ")
print("subtraction")
print("multiplication")
print("division")
print("exit")
def addition(n1,n2):
    c=n1+n2
    print(c)
def subtraction(n1,n2):
    c=n1-n2
    print(c)
def multiplication(n1,n2):
    c=n1*n2
    print(c)
def division(n1,n2):
    c=n1/n2
    print(c)
def exit():
    print("exit")
n1=int(input("enter first value:"))
n2=int(input("enter second value:"))
option=input("select any operator")
if option=="+":
    addition(n1=n1,n2=n2)
elif option=="-":
    subtraction(n1=n1,n2=n2)
elif option=="*":
    multiplication(n1=n1,n2=n2)
elif option=="/":
    division(n1=n1,n2=n2)
elif option=="exit":
    exit()
else:
    print("invalid input")
