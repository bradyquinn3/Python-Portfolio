
def main ():

       #define the list of grades
       grades = []
       count = 0

       #enter the first grade
       grade = float(input("Enter a grade or -1 to stop: "))

       #begin while loop
       while grade != -1:
                  grades.append(grade)
                  count += 1
       #enter the next grade
                  grade = float(input("Enter a grade or -1 to stop: "))
        
                #compute the average
       total = sum(grades)
       average = total / count


       print(f"there are {count} grades entered totaling {total: .2f}")
       print(f"The average grade is ${average: .2f}")


        #sort the grades
       print("sorting grades...")
       grades.sort()
        #print the sorted grades
       print("printing grades...")
       for item in grades:
           print(f"${item: .2f}")


        #reversing the order of grades
       print("reversing grades...")
       grades.reverse()

        #print the reversed grades
       print("printing reversed grades...")
       for item in grades:
            print(f"${item: .2f}")


        #highest and lowest grades
       print(f"The highest grade is {max(grades): .2f}")
       print(f"The lowest grade is {min(grades): .2f}")        

main()


