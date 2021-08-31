"""
Multiplication table
Use for statement(s) to:
  a)   print out the 6th multiplication table from 0 to 10 
  b)   let the user input the table, start and end of the table. 
  c)   print out a full multiplication table from 0 to 10.
"""

# a) print out the 6th multiplication table from 0 to 10 
"""
for i in range(0,11):
    num = 6*i
    print(f"6 * {i} = {num}")
"""


 # b) let the user input the table, start and end of the table. 
"""
x = int(input("Enter the lowest number in the multiplication table you want to print: "))
y = int(input("Enter the highest number in the multiplication table you want to print: "))
z = int(input("Enter the number you want to multiply with: "))

for i in range(x,y+1):
    num = z * i
    print(f"{z} * {i} = {num}")
 """


# c) print out a full multiplication table from 0 to 10.

nums = list(range(0,11))
nums2 = list(range(0,11))
sum = 0

for n1 in nums:
    for n2 in nums2:
        sum = n1 * n2
        print(f"{sum}", end=" ")
    print()