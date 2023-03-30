# Question # 6 Write a program that takes input two integer numbers and prints all the common divisors. For example if numbers entered are 100 and 80 then it should print 1,2,5, and 20 because
# divisors of 100 are 1, 2, 5, 10, 20, 50, 100 and divisors of 80 are 1, 2, 4, 5, 8, 16, 20, 40, 80. common of among them are 1,2, 5 and 20. As second test case if you enter 72 and 90 then it should print 1, 2, 3, 6, and 18 since divisors of
# 72 are 1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72 and divisors of 90 are 1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45. Object:

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
common_divisors = []

for i in range(1, min(num1, num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        common_divisors.append(i)

print(f"The common divisors of {num1} and {num2} are: {common_divisors}")
