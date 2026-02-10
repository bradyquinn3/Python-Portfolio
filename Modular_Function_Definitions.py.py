#there are three seating categories at a stadium. Class A costs $30, Class B costs $25, and Class C costs $20. Write a program that asks how many tickets for each class were sold. Then call a function that calculates (and returns) the total income from ticket sales.

#part 1: define constants for ticket prices
class_a_cost = 30
class_b_cost = 25
class_c_cost = 20

#part 2: create function to calculate income
def calculate_income (num_a, num_b, num_c):
    total = (num_a * class_a_cost) + (num_b * class_b_cost ) + (num_c * class_c_cost)
    return total

 #part 3: get th user input
def main ():
    class_a_num = int(input("How many tickets were bought for class A: "))
    class_b_num = int(input("How many tickets were bought for class B: "))
    class_c_num = int(input("How many tickets were bought for class C: "))

 #part 4: call function and print result
    total_income = calculate_income(class_a_num, class_b_num, class_c_num)
    print (f"your total income is ${total_income:.2f}")

#run the code
main ()
