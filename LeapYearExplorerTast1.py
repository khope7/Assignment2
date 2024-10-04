#Task 1: Leap Year Checker Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message.
#Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

#Writing arithmetic algorithm that catches for leap years

#Awaiting user input for year
your_year = int(input("Hello! Please enter a year so you can find out if your year entered is a leap year: "))

#Conditional statement catching for 4 year divisible catch, 100 non-catch, and 400 catch superceding 100 non-catch
if your_year % 4 == 0 and your_year % 100 != 0 or your_year % 400 == 0:
    print("Congratulations! The year you entered is a leap year! Your entered year:", your_year)
else:
    print("your number is not a leap year")