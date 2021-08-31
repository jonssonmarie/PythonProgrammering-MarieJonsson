"""
Rice on chessboard
In first square of the chessboard there is one grain of rice, 
in the second square there is two grains, 
in the third square there is four grains and so on. 
How many grains are there in the whole chessboard when all squares 
are filled using this pattern?
"""

no_rice = 1
for i in range(0,64):
    no_rice += (2**i)
print(no_rice)