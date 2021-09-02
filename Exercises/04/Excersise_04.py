"""
Chessboard 
  a) Create this list using list comprehension: 
     ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
  b) Create a 2D list to hold the coordinates in a chessboard. 
"""

# a) create list
alfabeth = ["A", "B", "C", "D", "E", "F", "G", "H"]

lst = []
for letter in alfabeth:
    letter_1 = letter + "1"
    lst.append(letter_1)
#print(lst)


# b) 2D list

col = []
for i in range(1,9):
    for letter in alfabeth:
        letter_x = letter + str(i)
        col.append(letter_x)

print([col[i:i+8] for i in range(0, len(col), 8)])

