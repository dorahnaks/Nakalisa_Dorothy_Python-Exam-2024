# No.1 (i)
def circle_area(r):
    pi = 3.14
    area = pi * r**2
    print(f"The area of the circle with radius {r} is: {area}")
circle_area(4)


# No.1 (ii)
def odd_number_sum():
    integers = [4, 7, 2, 9, 12, 15]
    sum_of_odd_numbers = 0
    for number in integers:
        if number % 2 != 0:
            sum_of_odd_numbers += number
    print(f"The sum of odd numbers is: {sum_of_odd_numbers}")
odd_number_sum()


# No.1 (iii)
def number_calculations():
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    
    number_sum = first_num + second_num
    number_difference = first_num - second_num
    number_product = first_num * second_num
    number_quotient = first_num / second_num
    
    print(f"\nThe sum ({first_num} + {second_num}) is: {number_sum}")
    print(f"\nThe difference ({first_num} - {second_num} ) is: {number_difference}")
    print(f"\nThe product ({first_num} * {second_num} ) is: {number_product}")
    print(f"\nThe quotient ({first_num} / {second_num} ) is: {number_quotient}")
    
number_calculations()


# No.1 (iv)

student_info = {'name': 'Alice', 'age':20, 'grade':'A'}  
student_info['age'] = 26
student_info['city'] = 'Kampala' 
print(student_info)