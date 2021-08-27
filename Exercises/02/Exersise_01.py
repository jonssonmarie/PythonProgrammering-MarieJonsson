"""
Count numbers (*)
Use a while statement to count from -10 to 10 with one increment.
"""

n = -11
n_lst = []

while -12 < n < 10:
    n += 1
    n_lst.append(n)
    print(f"{n}", end=", ", sep = "\n")

print ("\n Another print as tuple")
print(f"{tuple(n_lst)}")