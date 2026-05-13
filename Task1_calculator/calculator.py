print("===== SIMPLE CALCULATOR =====")

num1 =float(input("enter first number:"))
num2 =float(input("enter second number:"))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponential")
print("6.Modulus")

choice =input("Choose operation(1/2/3/4/5/6):")

if choice =="1":
    print("Result",num1+num2)

elif choice =="2":
    print("Result",num1-num2)

elif choice =="3":
    print("Result",num1*num2)

elif choice =="4":
    print("Result",num1/num2)

elif choice =="5":
    print("Result",num1**num2)

elif choice =="6":
    if num2!=0:
        print("Result",num1%num2)
    else:
        print("Division by zero is not allowed")   

else:
    print("invalid choice")