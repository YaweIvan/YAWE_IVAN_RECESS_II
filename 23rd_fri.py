#functions

def add_numbers(x,y):
    result = x+y
    print('sum:', result)
    
add_numbers(15, 30)

#write a function of three values:
def product(x,y,z):
    result = x*y*z
    print("product:",result)
    
product(2,4,6)

#return values
#return statement ends the function execution and sends the value back 

#return multiple values
def get_stats(a,b):
    return a+b,a-b
sum_value, subtract_value = get_stats(20,12)
print("sum:", sum_value)
print("subtrcat:", subtract_value)

#use return to divide two values using a function Exercise
def divide_numbers(a,b):
    return a/b
answer=divide_numbers(4,2)
print("answer:", answer)

#lambda function
#use it for small functions , we use lambda keyword

def square(x): return x*x
print(square(5))

#add multiple arguements
add = lambda a, b : a+b
print(add(10,5))

#use lambda functiom to get square of list map [1, 2, 3, 4, 5]
# square = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))

#maps
numbers =[1, 2, 3, 4, 5]
squared = list(map(lambda x: x*x, numbers))
print(squared)

#ass find the factorial of a number (5!)

##Error Handling
#python error handling

#types of errors 
#syntax 
#runtime 5/0
#logical : program runs but get wrong output 

# block of codes try, except, else and finally 

#Example ..try to divide 5/0(causes ZeroDivisionError)
try:
    result = 5/0
except ZeroDivisionError:
    print("Cannot divide by 0")
    
else:
    print("division successful", result)
    
finally:
    print("run completed")
    
##raise a custom exception that checks for positive number
#soln on a custom error 

class NotPositiveError(Exception):
    pass
#function to check if number is positive
def check_positive(number):
    if number <= 0:
        raise NotPositiveError("Not positive number")
    else:
        print("Nice shit..its a positive number")
#usage..in example
#we use try......except
try:
    num = int(input("Enter a positive number😊: "))
    check_positive(num)
except NotPositiveError as e:
    print("custom error:", e)
except ValueError:
    print("please enter a valid number😒")
            


##Ass2
#write a program to handle errors, the program to ask for two numbers using input and then 
#divides them. use an infinite loop to keep asking until a valid input is provided
