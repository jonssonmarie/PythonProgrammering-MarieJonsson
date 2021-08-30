"""
Check convergence
Use a while statement to compute the following sums:
a) sum = 1 + 1/2 + 1/4 + 1/8 + ... + 1/2^n
b) sum = 1 - 1/3 + 1/5 - 1/7 + ... + (-1)^n/2n+1

Try different values on n to see which value it converges to.
"""
#a)

n = int(input(" Enter the number of terms: "))
sum1 = 1
denom = 1
i = 0

while i <= n:
    # nämnaren (denominator) kvaderas vid varje loop, n ger hur många ggr den ska kvadreras
    sum1 += (1/(denom*2))
    i += 1
    denom *= 2
print("Statement converge to:", sum1)