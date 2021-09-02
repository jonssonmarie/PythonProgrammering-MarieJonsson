"""
Food menu
Create a:
  a)   list with the following elements: 
       "vegetarisk lasagne", "spaghetti", "fisk", "grönsakssoppa", "pannkakor".
  b)   list with the weekdays
  c)   create a food menu with each day corresponding to each 
       food item and print it out.
"""
# a)  List with elements
food = ["vegetarisk lasagne", "spaghetti", "fisk", "grönsakssoppa", "pannkakor"]

# b) weekdays

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# c) food menu

menu = []

for f, day in zip(food, weekdays):
    m = [day, f]
    menu.append(m)
    
print(f"Menu: {menu}")
print()

# c) alternative
