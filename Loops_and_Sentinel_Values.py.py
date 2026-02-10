#1 Write a program that takes in a series of numbers and computes the average of those numbers. Use -1 as a stop value (sentinel). Be sure to display the average.
from math import factorial


happiness_level = float(input("what is your happiness level (1-10): "))
total_happiness_level = 0
answers = 0

while happiness_level != -1:

    total_happiness_level = total_happiness_level + happiness_level
    answers = answers + 1

    happiness_level = float(input("what is your happiness level (1-10): "))

average = total_happiness_level / answers
print ("the average happiness level is", average)

#2 Write a program that calculates how much money a person would earn over a period of time if their salary is one penny the first day, two cents the second day, four cents the third day, and continues to double each day. The program should ask the user for the number of days. Display a table showing what the salary is for each day and the total pay at the end of the period. Be sure to display the output formatted as dollar amounts, not number of pennies.

#2
days = int(input("how many days did you work? "))
salary = 1
total_pay = 0

for day in range(1, days + 1):
    print(f"Day {day}: ${salary / 100:.2f}")  # Show salary in dollars
    total_pay += salary                       # Add to total
    salary *= 2                               # Double for next day

print(f"Total pay: ${total_pay / 100:.2f}")

#Write a program that takes a number (n) and computes the factorial (n!) of a nonnegative integer.Use a for loop to run the calculation

n = int(input("what number would you like to be factorialed (n!)? "))
factorial = 1

for number in range(1, n + 1):
    factorial *= number

print (factorial)
    



