num1=float(input("enter your first number :  "))
oper=input("enter operator sign :")
num2=float(input("enter your second number :  "))
if oper=="+":
    print(num1+num2)
elif oper =="-":
    print(num1-num2)
elif oper =="/":
    print(num1/num2)
elif oper=="*":
    print(num1*num2)
else:
    print("enter a valid operator")               