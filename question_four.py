'''
# No.4 (i)(a)

Object Oriented Programming invoves the used of classes and objects.

- OOP helps programmers classfy different attributes
- OOP aids software developers who deal with multiple things that are related to one another to make programs that unify them


# No.4 (i)(b)

A class refers to a container of different methods and objects
An object is part of a class. You can have multiple objects of the safe class.

'''

# No.4 (ii)

sentence = input("Enter sentence: ")
occurences = sentence.split()
print(occurences)


occurence_dict = {}

for word in sentence:
    pass


# No.4 (iii)

def number_sum(a, b):
    sum_of_numbers = a + b
    print(f"The sum of {a} and {b} is: {sum_of_numbers}")
number_sum(3, 4)

 
 # No.4 (iv)
 
class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color
# No.4 (v)

    def start_engine(self):
        print("The engine of the car has started")

car_1 = Car('Toyota', 'Hammer', 'Silver')
print(f"The car brand is: {car_1.brand}")
print(f"The car name is: {car_1.name}")
print(f"The color of the car is: {car_1.color}")
car_1.start_engine()

            