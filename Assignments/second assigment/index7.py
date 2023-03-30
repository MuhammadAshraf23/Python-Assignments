# Question # 7  Extend the logic of last object to write a program that takes input two integer numbers and prints
# Highest Common Factor that is also called Greatest Common Divisor all the common divisors. For example if numbers entered are 100 and 80 then it should 20 because divisors of 100 are 1, 2, 5, 10, 20, 50, 100 and divisors of 80 are 1, 2, 4, 5, 8, 16, 20, 40, 80. common of among them are
# 1,2, 5 and 20. As second test case if you enter 72 and 90 then it should print 18 since divisors of 72 are 1, 2, 3, 4,



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
