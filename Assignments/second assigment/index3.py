#  Q # 3    Write a Python program that prints each item and its corresponding type from the following list.

my_list = [1, 2.0, "three","Arykaz" [4, 5], (6, 7), {"eight": 8, "nine": 9}]

for item in my_list:
    print(f"{item} is of type {type(item)}")