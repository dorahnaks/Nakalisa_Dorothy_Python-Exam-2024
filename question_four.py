'''
# No.4 (i)(a)
# No.4 (i)(b)
'''

# No.4 (ii)

# sentence = input("Enter sentence: ")


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

            