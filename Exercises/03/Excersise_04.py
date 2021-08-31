"""
Faculty
Use a for statement to compute n!
n! = 1 * 2 * 3 * ...* (n-1)n 
Let the user input n.
"""

n = int(input("Enter the faculty you want to compute: "))
sum_ = 1

for i in range(1, n+1):
    sum_ = sum_*i
print(sum_)
