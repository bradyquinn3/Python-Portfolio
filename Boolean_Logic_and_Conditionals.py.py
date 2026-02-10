#1. Write a program that takes in two names and prints out which one comes first alphabetically.
#2. Write a program that takes three numbers and returns the lowest number. 
#3. Write a program that takes in a person’s age and prints out whether that person is a teenager

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

if name1 < name2:
    print(f"{name1} comes before {name2} alphabetically.")
elif name1 > name2:
    print(f"{name2} comes before {name1} alphabetically.")
else:
    print("Both names are the same.")

#2. Write a program that takes three numbers and returns the lowest number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
lowest = min(num1, num2, num3)
print(f"The lowest number is: {lowest}")

# 3. Write a program that takes in a person’s age and prints out whether that person is a teenager
age = int(input("Enter the person's age: "))
if 13 <= age <= 19:
        print("The person is a teenager.")
else:
        print("The person is not a teenager.")
