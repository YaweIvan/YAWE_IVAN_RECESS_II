while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the  second number: "))
        result = num1/num2
        print(f"The result of {num1} divided by {num2} is {result}")
        break # exit loop
    
    except ValueError:
        print("Enter valid numbers eg(5, 3.4)")
    except ZeroDivisionError:
        print("cannot divide by zero!! try another number ")