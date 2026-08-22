num1=float(input("Enter a number:"))
num2=float(input("Enter a number:"))
operation=input("Enter the operation to be performed(+,*,-,/):")
#Performs Addition(+) of two numbers.
if operation=="+":
	calculate=num1+num2
	print(calculate)
#Performs Subtraction(-) of two numbers.
elif operation=="-":
	calculate=num1-num2
	print(calculate)
#Performs Multiplication(*) of two numbers.
elif operation=="*":
	calculate=num1*num2
	print(calculate)
#Performs Division(/) of two numbers.
elif operation=="/":
	if num2==0:
	    print("Cannot divide by zero")
	else:
	    calculate=num1/num2
	    print(calculate)
else:
    print("Invalid Operator")
    
