n = input(" Name of Student :")
Sql = int(input(" enter Sql number : "))
Python = int(input("enter python numbers :"))
English = int(input(" enter english number:"))

if Sql > 100 or English > 100 or Python > 100:
    print("It's out of marks " )
    
elif Sql < 0 or English < 0 or Python < 0:
    print("negative marks are not allowed ")
       
else:
    total = Sql + Python + English
    percentage = (total / 300) * 100
    
    print("\nName of Student:", n)
    print("Total Marks:", total)
    print("Percentage:", percentage)

    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 80:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: C")
    elif percentage >= 60:
        print("Grade: D")
    else:
        print("Grade: Please work hard, you have failed")
    
if Sql > Python and Sql > English:
    print("Sql is the highest subject.")
elif Python > Sql and Python > English:
    print("Python is the highest subject.")
elif English > Sql and English > Python:
    print("English is the highest subject.")
elif Sql == Python and Sql > English:
    print("Sql and Python are the highest subjects.")
elif English == Sql and English > Python:
    print("English and Sql are the highest subjects.")
elif English == Python and English > Sql:
    print("English and Python are the highest subjects.")
else:
    print("All subjects have equal marks.")    

if Sql < 35 or Python < 35 or English < 35:
    
    if Sql < Python and Sql < English:
        print("Sql is the lowest subject.")
    elif Python < Sql and Python < English:
        print("Python is the lowest subject.")
    elif English < Sql and English < Python:
        print("English is the lowest subject.")
    elif Sql == Python and Sql < English:
        print("Sql and Python are the lowest subjects.")
    elif English == Sql and English < Python:
        print("English and Sql are the lowest subjects.")
    elif English == Python and English < Sql:
        print("English and Python are the lowest subjects.")
    else:
       print("All subjects have equal marks.")

else:
    print("Student has passed in all subjects.")       
    
Average = total / 3
print("Average marks of student is:", Average)

if percentage >= 75 :
    print("Student is Eligible for scholarship") 
else:
    print("Student is not Eligible for scholarship")    
    