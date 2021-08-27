# Right angle
# Ask the user to input three angles and check if the triangle has a right angle. 
# Your code should make sure that all three angles are valid and make up a triangle.

angles = input("Enter three angles, separated by , :")

ang_lst = angles.split(",")

angle_1 = int(ang_lst[0])
angle_2 = int(ang_lst[1])
angle_3 = int(ang_lst[2])

# check if the sum of angles are 180 deg
sum_angles = angle_1 + angle_2 + angle_3

if sum_angles == 180:
    # Check if any ore more angles is 90 deg
    if angle_1 != 90:
        if angle_2 != 90:
            if angle_3 == 90:
                print("This is a right angle triangle ")
    if angle_2 != 90:
        if angle_3 != 90:
            if angle_1 == 90:
                print("This is a right angle triangle ")
    if angle_3 != 90:
        if angle_1 != 90:
            if angle_2 == 90:
                print("This is a right angle triangle ")
    if angle_3 != 90:
        if angle_1 != 90:
            if angle_2 != 90:
                print("This is not a right angle triangle ")

else:
    print("This is not a right angle triangle ")
