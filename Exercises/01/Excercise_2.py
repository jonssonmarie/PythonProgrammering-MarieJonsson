# Smallest
# Ask the user to input two numbers and check which one 
# is the smallest and print it out.

numbers = input("Enter two integers separated with ,  : ")
num_list = numbers.split(",")

num_1 = int(num_list[0])
num_2 = int(num_list[1])

if num_1 == num_2:
    print(f"{num_1} and {num_2} is equal")
if num_1 < num_2:
    print(f"{num_1} is the smallest number")
else:
    print(f"{num_2} is the smallest number")
