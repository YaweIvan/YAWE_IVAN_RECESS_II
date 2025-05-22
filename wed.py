# Condition Statements
age = 18
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

print()  # just for spacing

# Passmark Exercise
passmark = 50

if passmark < 50:
    print("Retake")
elif passmark >= 50 and passmark < 80:
    print("Passed")
else:
    print("Excellent")

print()  # spacing

# Nested If
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
    has_ticket = input("Do you have a valid ticket? (yes/no): ")
    if has_ticket.lower() == "yes":
        print("You can watch the movie.")
    else:
        print("You cannot watch the movie without a ticket.")
else:
    print("You are not allowed to watch the movie because you are underage.")

print()  # spacing

# Loop: Print numbers 0 to 4
for i in range(5):
    print(i)

print()  # spacing

# Loop to enter car names
cars = []
for i in range(5):
    car = input(f"Enter name of car {i + 1}: ")
    cars.append(car)

print("\nList of cars entered:")
for car in cars:
    print(car)

# print()  # spacing

# Loop through predefined list of cars
cars = ['Ipsum', 'Probox', 'Sienta', 'Pickup']
print("Predefined list of cars:")
for car in cars:
    print(car)

# using while loop
count=1
while count >=5:
    print(count)

#breakstatemt
count=1
while count <= 5:
    if count == 4:
        break
    print(count)
    count+=1
    

#continue statement 
i =0
while i<5:
    i+=1
    if i ==3:
        continue
    print(i)

#example
num = 6
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    input_num = int(input(f"Guess a number between 1 to 10 (Attempt {attempts + 1}/{max_attempts}): "))
    attempts += 1

    if input_num == num:
        print(f"Guessed right! It's indeed {num}! You won in {attempts} attempt(s).")
        break
    else:
        if attempts < max_attempts:
            print(f"Incorrect! Try again. You have {max_attempts - attempts} attempt(s) left.")
        else:
            print(f"Sorry, you didn't guess it. The correct number was {num}. Better luck next time!")


#comprehensions
#list and dictionary comprehensions 

square =[X**2 for X in range(10)]
print(square)

#example ..list comprehension with condition
numbers=[1, 2, 3, 4, 5]
square_dict = {X: X**2 for X in numbers}#dictionary with {}
print(square_dict)

#condition : must be even number
even_square=[X**2 for X in range(10) if X%2==0]
print(even_square)


#exercise realworld example
#create an ATM withdraw program to use if , else statemnets to check account balance before allowing withdrawal
# ass create an inventory management: use loops to display or update a list of stock items 

#1
account_balance=10000
withdraw_amount=int(input("How much do u want to withdraw"))
if withdraw_amount<=account_balance:
    account_balance-=withdraw_amount
    print("take your card")
    print("your new balance is:", account_balance)
else:
    print("you dont have enough money on account")
    print("your balance is", account_balance)