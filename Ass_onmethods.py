#Method overriding 
class Animal:
    def speak(self):
        print("Animal speaks")
        
class Dog:
    def speak(self):
        print("Dog barks")
        
#test
a = Animal()
a.speak()

d = Dog()
d.speak()


#method overloading
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Test
calc = Calculator()
print(calc.add(2))        # Output: 2
print(calc.add(2, 3))     # Output: 5
print(calc.add(2, 3, 4))  # Output: 9



class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# Test
d = D()
d.show()  # Output: B

# Show MRO
print(D.__mro__)
    
    
    
