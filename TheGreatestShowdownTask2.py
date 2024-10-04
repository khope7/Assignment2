#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

#Created 3 tier entry code for user with type float to catch for incomplete number user entries
number1 = float(input("Enter 3 prodigious numbers for the Greatest Showdown of all time! " ))

first_number = number1

number2 = float(input())

second_number = number2

number3 = float(input())

third_number = number3

#Conditional statement that returns greatest number based on entries
if first_number >= second_number and first_number >= third_number:
    print("Congratulations! your first number was the greatest! Your number: ", first_number)
elif second_number >= first_number and second_number >= third_number:
    print("Congratulations! your second number was the greatest! Your number: ", second_number)
else:
    print("Congratulations! your third number was the greatest! Your number: ", third_number)

#Conditional statement that returns smallest number based on entries
if first_number <= second_number and first_number <= third_number:
    print("Also, your first number was the smallest! Your number: ", first_number)
elif second_number <= first_number and second_number <= third_number:
    print("Also, your second number was the smallest! Your number: ", second_number)
else:
    print("Also, your third number was the smallest! Your number: ", third_number)