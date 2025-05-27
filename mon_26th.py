#Abstraction
# Import the ABC and the abstractmethod 

from abc import ABC, abstractmethod



#eg starting a car engine and bike 
#define abstract class(ABC)
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass # start has no implemetation
    
    #child class implementing the abstract method
class Car(Vehicle):
    def start(self):
        print("Car engine starts")
        
class Bike(Vehicle):
    def start(self):
        print("Bike engine starts")

# Notes :
# We cannot create object of abstract class
# Demo Live:
# vehicle1 = vehicle() # This would raise an error

# Accepted : Create objects iof subclass
            
car1 = Car()
bike1 = Bike()         
            
 # Display output of the methods we would use
# Calling start method

car1.start()
bike1.start()
           
 #exercise
 #submit your work on github on method overriding, method overloading and MRO
            
            
 #for jeff..Banking System, Bank Accounts.. real world application
 #for us.. University Sysytem
            
 #Banking System 
 #Bank account: saving account and current account inherit from Account
 #deposit, withdraw, display balance, types of accounts
            
         
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Account {self.account_number} Balance: {self.balance}")


# Subclass: SavingAccount
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate / 100  # Convert percent to decimal

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added. New balance: {self.balance}")


# Subclass: CurrentAccount
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}')
        else:
            print('Exceeded the overdraft limit.')


#  Create objects and test 

saving = SavingAccount('SAV0555555', 100000, 5)
current = CurrentAccount('CUR0577777', 50000, 10000)

# Test Methods
saving.display_balance()
saving.add_interest()
saving.withdraw(20000)

print('----------------------------')

current.display_balance()
current.withdraw(70000)
current.withdraw(45000)

                    
        #universty system to diplay information 
        #classses : 