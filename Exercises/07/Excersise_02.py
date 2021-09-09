"""
Find errors
Find the errors in this code. Just change the function, don't touch the test program.

def is_fourdigit(number):
    if number//1000 < 10
        return true
    else 
        return false

# test program
test_numbers = [231, 3124, -4124, -1000,-999, 1001, 10000, -10000, 999]

for number in test_numbers:
    if is_fourdigit(number):
        print(f"{number} is four-digit")
    else:
        print(f"{number} is not four-digit")
"""

"""
Svar: 
rad 6: alla heltal under 10 sorteras bort (behandlas inte) och : saknas
rad 7: t ska vara stor bokstav -> True
rad 8: : efter else
rad 9: f skal vara stor bokstab -> False

Fixad: 
def is_fourdigit(number):
    if number//1000 < 10:
        return True
    else: 
        return False

# test program
test_numbers = [231, 3124, -4124, -1000,-999, 1001, 10000, -10000, 999]

for number in test_numbers:
    if is_fourdigit(number):
        print(f"{number} is four-digit")
    else:
        print(f"{number} is not four-digit")
"""

