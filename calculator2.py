def calculator():
    while True:
        num1=int(input("Enter first number"))
        op=input("Enter operation")
        num2=int(input("Enter second number"))

        if op=="+":
            result=num1+num2
        elif op=="-":
            result=num1-num2
        elif op=="/":
            result=num1/num2
        elif op=="*":
            result=num1*num2
        else:
            print("invalid option")
            continue
        print("Result is: ",result)
        break

calculator()

