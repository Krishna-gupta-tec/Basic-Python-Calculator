# Author:Krishna
# Date:9/7/2025

print("Wecome to The Calculator".center(50,"-"))

num1 = int(input("Enter The value of num1:\n")) #it ask the user for first num value
num2 = int(input("Enter The value of num2:\n")) # then it ask the user for second value
operator = input("Choose an operator from (1-4)\n1.+\n2.-\n3.*\n4./\n") # it ask user to choose an operator to perform calucution with that 
#given two numebers (say user entered num1=3,and num2=5) and if user choose 1 it perform calulation acc to condition in our condition the
#value is adding means 3+5 = 8

if  operator == "1":
    print(f"The value of {num1} + {num2} is {num1 + num2}")

elif operator == "2":
    print(f"The value of {num1} - {num2} is {num1 - num2}")
   
elif operator == "3":
    print(f"The value of {num1} * {num2} is {num1 * num2}") 
    
elif operator == "4":
    print(f'The value of {num1} / {num2} is {num1 / num2}')
    
else:
    print(f"Invalid operator")  # if user choose something that the condition has not asked to enter it gives error like if i choose 6 it give
    #error.             
