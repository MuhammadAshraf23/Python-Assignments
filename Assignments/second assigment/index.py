                   #Q1 Write a Python program to find those numbers which are divisible by 7 and multiple of
for num in range(1500, 2700):
    if num % 7 == 0 and num % 5 == 0:
      print(num)
                      ############################QUESTION END#########################################
        
                   #Q2 Write a program that prints Factorial of a user given integer without using math.factorial() function.
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num+1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")
                           ############################QUESTION END#########################################
    
             #Q3 Write a Python program that prints each item and its corresponding type from the following list.
my_list = [1, 2.0, "three","Arykaz" [4, 5], (6, 7), {"eight": 8, "nine": 9}]
for item in my_list:
    print(f"{item} is of type {type(item)}")
                        ############################QUESTION END#########################################
        
            #Q4Write a Python program to find numbers between 100 and 400 (both included) where each digit  of a number is an even number. 
            # The numbers obtained should be printed in a comma-separated sequence
results = []
for num in range(100, 401):
    digits = [int(digit) for digit in str(num)]
    if all(digit % 2 == 0 for digit in digits):
        results.append(str(num))
print(", ".join(results))
                       ############################QUESTION END#########################################
    
               #Q5 Write a program that takes input an integer number and print all of its Divisors. Object:
num = int(input("Enter a number: "))
divisors = []
for i in range(1, num+1):
    if num % i == 0:
        divisors.append(i)
print(f"The divisors of {num} are: {divisors}")
                      ############################QUESTION END#########################################

             #Q6 Write a program that takes input two integer numbers and prints all the common divisors. For example if numbers entered are 100 and 80
             # then it should print 1,2,5, and 20 because divisors of 100 are 1, 2, 5, 10, 20, 50, 100 and divisors of 80 are 1, 2, 4, 5, 8, 16, 20, 40, 80.
             #  common of among them are 1,2, 5 and 20. As second test case if you enter 72 and 90 then it should print 1, 2, 3, 6, and 18 since divisors of 72  
             # are 1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72 and divisors of 90 are 1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45. Objec t:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
common_divisors = []
for i in range(1, min(num1, num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        common_divisors.append(i)
print(f"The common divisors of {num1} and {num2} are: {common_divisors}")
                                 ############################QUESTION END#########################################
    
                       # Q7 Extend the logic of last object to write a program that takes input two integer numbers and prints
                       # Highest Common Factor that is also called Greatest Common Divisor all the common divisors. For example if numbers entered are 100 and 80 
                       #then it should 20 because divisors of 100 are 1, 2, 5, 10, 20, 50, 100 and divisors of 80 are 1, 2, 4, 5, 8, 16, 20, 40, 80. common of
                       # among them are 1,2, 5 and 20. As second test case if you enter 72 and 90 then it should print 18 since divisors of 72 are 1, 2, 3, 4,
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
common_divisors = []

for i in range(1, min(num1, num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        common_divisors.append(i)
if len(common_divisors) > 0:
    hcf = max(common_divisors)
    print(f"The highest common factor of {num1} and {num2} is: {hcf}")
else:
    print(f"{num1} and {num2} have no common divisors.")
    ############################QUESTION END#########################################
    
