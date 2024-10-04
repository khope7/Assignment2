#Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.

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