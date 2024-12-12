# No.2 (i)

student_name = input('Enter the Student name: ')
student_number = input('Enter the Student Number: ')

programming = int(input('Enter the Programming score: '))
data_science = int(input('Enter the Data Science score: '))
computer_applications = int(input('Enter the Computer Application score: '))

average_mark = (programming + data_science +computer_applications) / 3

print(f"The average mark is: {average_mark:.3f}")
print(f"The Student name is {student_name} and the Student Number is {student_number}.")
print(f"The Following are the marks for {student_name}")
print(f"Programming: {programming}")
print(f"Data Science: {data_science}")
print(f"Computer Application: {computer_applications}")


# No.2 (ii)

def miles_per_gallon():
    miles_driven = int(input("Enter the miles driven: "))
    gallons_of_gas_used = int(input("Enter the gallons of gas used: ")) 
    miles_per_gallon_used = miles_driven / gallons_of_gas_used
    print(f"The MPG (miles per gallon used) is: {miles_per_gallon_used}")
    
miles_per_gallon()


# No.2 (iii)

def numbers_divisable_by_2():
    for num in range (1, 101):
        if num % 2 != 0:
            print(num)
numbers_divisable_by_2()