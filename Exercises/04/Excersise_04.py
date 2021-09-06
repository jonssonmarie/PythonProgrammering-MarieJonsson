"""
Chessboard 
  a) Create this list using list comprehension: 
     ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
  b) Create a 2D list to hold the coordinates in a chessboard. 
"""

# a) create list
alfabeth = ["A", "B", "C", "D", "E", "F", "G", "H"]

letter_1 = [letter + "1" for letter in alfabeth]
print(f"Lista: {letter_1}")

# Alternativ utan list comprehension
"""lst = []
for letter in alfabeth:
    letter_1 = letter + "1"
    lst.append(letter_1)
#print(lst)
"""

# b) 2D list
print("2D list:")

# Med list comrehension:
[[f"{char}{i}" for char in alfabeth] for i in range(1,9)]
