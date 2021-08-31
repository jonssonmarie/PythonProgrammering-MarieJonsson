"""
Arithmetic sum
Use a for statement to compute the following sums:
  a) sum = 1 + 2 + ... + 99+ 100
  b) sum = 1 + 3 + 5 + ... + 97 + 99
"""

# a)
sum1 = 0
for i in range(1,101):
    sum1 += i

print(f"{sum1}", end = "")

print()

# b)
sum2 = 0
for i in range(1,101,2):
    sum2 += i
print(f"{sum2}", end = " ")