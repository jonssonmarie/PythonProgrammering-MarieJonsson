"""
Arithmetic sum
Use a while statement to compute the following sums:
  a)   text{sum} = 1 + 2 + ... + 99+ 100
  b)   text{sum} = 1 + 3 + 5 + ... + 97 + 99
"""
# a)

n = 0
sum = 0

while 0 <= n < 100:
    sum += n
    n += 1
print(sum, n)

# b)

n = -1
sum = 1
while n < 99:
    sum += n
    n += 2

print(sum, n)