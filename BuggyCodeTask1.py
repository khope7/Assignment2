#Task 1: Code Correction You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

#Buggy Code:

#number = input("Enter a number: ")

#if number > 0:
#    print("The number is positive.")
#elif number = 0:
#    print("The number is zero.")
#else number < 0:
#    print("The number is negative.")

#Writing corrected code (used https://stackoverflow.com/questions/31368624/condition-checking-in-python-with-user-input) for reference, used float to catch for decimal entries, alternative to float would be int for whole numbers
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")