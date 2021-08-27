# user questions:
l_weight = float(input("Enter the luggage weight: "))
l_length = float(input("Enter the luggage length: "))
l_width = float(input("Enter the luggage width: "))
l_height = float(input("Enter the luggage height: "))

# max allowed settings in variables
max_weight = 8  # kg
# cm
max_length = 55
max_width = 40
max_height = 23

if l_weight > max_weight:
    print("To high weight on luggage")
elif l_length > max_length:
    print("Luggage exceeds max length")
elif l_width > max_width:
    print("Luggage exceeds max width")
elif l_height > max_height:
    print("Luggage exceeds max height")
else:
    print("Welcome, you can check in! ")