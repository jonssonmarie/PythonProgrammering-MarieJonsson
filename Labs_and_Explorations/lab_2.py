"""
Grundläggande:
1. Läs in datan
2. spara i lämplig datastruktur
3. Plotta alla punkter i samma fönster med med olika färger
4. Läs in testpunkterna
5. Beräkna avstånd mellan testpunkterna
6. Närmast punkten tillhör Pichu?
6a. NEJ -> Klassifiera testpunkt som Pichu
6b. JA -> Klassificera testpunkt som Pikachu
Steg 2:
1. Låt användaren mata in en testpunkt och avgör om den dess klass. Ta med felhanteringen
som tar hand om negativa tal och icke-numeriska inputs. Se till att ha användarvänliga felmeddelanden.
2. Den approachen vi använt med närmaste punkten kan klassificera fel när punkterna för
respektive klass går in i varandra. Nu ska du istället välja de fem närmaste punkterna till din
testpunkt. Den klass testpunkten tillhör avgörs av majoritetsklassen av de närmaste punkterna.
Steg 3:
Bonusuppgifter (frivilliga)
3. Dela in ursprungsdatan slumpmässigt så att:
    90 är träningsdata (45 Pikachu, 45 Pichu)
    10 är testdata (5 Pikachu, 5 Pichu)
4. Beräkna noggranheten genom följande formel: accuracy = TP + TN / TOTAL
"""

import matplotlib.pyplot as plt
import math
import random as rnd

# paths to files
pichu_path = "C://Users//trull//Desktop//ITHS//Lab2//pichu.txt"
pikachu_path = "C://Users//trull//Documents//Lab2//pikachu.txt"
test_points_path = "C://Users//trull//Desktop//ITHS//Lab2//test_points.txt"

# open and read files
with open(pichu_path, 'r') as pichu, open(pikachu_path, 'r') as pikachu, open(test_points_path, 'r') as test_point:
    pichu_points = pichu.readlines()[1:]
    pikachu_points = pikachu.readlines()[1:]
    test_points = test_point.readlines()


while True:
    user = input("Enter a point and see which class it belongs to: ")
    try:
        user_data = []      # list for user_data
        coord = user.split(",")

        if len(coord) <= 2:
            for c in coord:
                cc = float(c)
                if cc <= 0.0:
                    raise Exception("Please use positive coordinates!")
                else:
                    point = float(cc)
                    user_data.append(point)
                    continue
            break
        else:
            print("Please enter ONE point with number, separated with comma eg: 29.05678, 36.578687")
            continue
    except ValueError as err:
        print(f"\nExplanation: {err}")
        print(f"Please enter ONE point with numbers, separated with comma eg: 29.05678, 36.578687\n")
        continue


# folders for sort_data function
test_data = []
pichu_sort = []
pikachu_sort = []


# Sort and clean data from Pichu and Pikachu
def sort_data(data_files, name, folder):
    for file in data_files:
        if data_files != test_points:
            file_clean = (file.replace("(", "").replace(")", "").replace("\n", "").replace(" ", "").replace("cm", ""))\
                .split(",")
            width = float(file_clean[0])
            height = float(file_clean[1])
            val = [[width, height], name]
            folder.append(val)
        else:
            file_split = file.split(",")
            for fil in file_split:
                file_clean = fil.replace("(", "").replace(")", "").replace(" ", "")
                l = float(file_clean)
                test_data.append(l)


sort_data(test_points, "", "")
sort_data(pichu_points, "pichu", pichu_sort)
sort_data(pikachu_points, "pikachu", pikachu_sort)


# Lists with randomly chosen traning data and test data ------------- ACCURACY ---------------------
accuracy_pichu = rnd.sample(pichu_sort, 45)
accuracy_pikachu = rnd.sample(pikachu_sort, 45)
test_accurracy_pichu = rnd.sample(pichu_sort, 5)
test_accurracy_pikachu = rnd.sample(pikachu_sort, 5)

# test_accuracy files with only coordinates, str is removed
test_acc_pichu_coord = [x[0] for x in test_accurracy_pichu]
test_acc_pikachu_coord = [x[0] for x in test_accurracy_pikachu]

# all test points for accuracy calculation
test_acc_w_h = test_acc_pichu_coord
for c in test_acc_pikachu_coord:
    test_acc_w_h.append(c)


# Test points data sorted by width and height  ----------------------- TEST DATA --------------------
test_data_width = test_data[0:len(test_data):2]
test_data_height = test_data[1:len(test_data):2]

test_data_w_h = []  # list for all test points width, height


# Test points data is looped to one list
def width_height_test_data(width_test, height_test):
    for (width, height) in zip(width_test, height_test):
        val = [width, height]
        test_data_w_h.append(val)


width_height_test_data(test_data_width, test_data_height)


# lists for euclidean_distance
all_tp = []
distance_pichu = []
distance_pikachu = []
dist_acc_pichu = []
dist_acc_pikachu = []


# calculate the euklidian distance, parameter folder is used to set name on the lists to separate data
def euclidean_distance(data_p, data_test, folder):
    for d in data_p:
        d_p = d[0]
        for test in data_test:
            dist = math.sqrt(math.pow((test[0]-d_p[0]), 2) + (math.pow((test[1]-d_p[1]), 2)))
            tp_dist = [dist, test]
            all_dist = [dist, data_p[0][1]]
            folder.append(all_dist)
            all_tp.append(tp_dist)


euclidean_distance(pichu_sort, test_data_w_h, distance_pichu)
euclidean_distance(pikachu_sort, test_data_w_h, distance_pikachu)
euclidean_distance(accuracy_pichu, test_acc_w_h, dist_acc_pichu)
euclidean_distance(accuracy_pikachu, test_acc_w_h, dist_acc_pikachu)


# sort data for ONE point and check class and print
def sort_for_user_data_one(distance_1, distance_2):
    sort_dist_1 = sorted(distance_1)[0:1]
    sort_dist_2 = sorted(distance_2)[0:1]
    if sort_dist_1[0][0] < sort_dist_2[0][0]:
        print(f"\nFor one point test - The point {user_data} belongs to class Pichu\n")
    else:
        print(f"\nFor one point test - The point {user_data} belongs to class Pikachu\n")


sort_for_user_data_one(distance_pichu, distance_pikachu)


# sort and reduce to eg. 5 closest after the calculated distances
sort_dist_pichu = sorted(distance_pichu)[0:5]
sort_dist_pikachu = sorted(distance_pikachu)[0:5]
sort_dist_acc_pichu = sorted(dist_acc_pichu)[0:10]       # 10 -----
sort_dist_acc_pikachu = sorted(dist_acc_pikachu)[0:10]   # 10 -----


# zip two lists elem by elem and then compare and measure how many pichu vs pikachu there is
belong_pichu = []
belong_pikachu = []
belong_acc_pichu = []
belong_acc_pikachu = []


# sort data for number of points > 1 by comparing distance
def sort_for_user_data_five(distance_1, distance_2, folder_1, folder_2):
    comp_list = []
    for (dist1, dist2) in zip(distance_1, distance_2):
        val = [dist1, dist2]
        comp_list.append(val)

    for elem in comp_list:
        if elem[0][0] < elem[1][0]:
            folder_1.append("1")
        else:
            folder_2.append("1")


sort_for_user_data_five(sort_dist_pichu, sort_dist_pikachu, belong_pichu, belong_pikachu)
sort_for_user_data_five(sort_dist_acc_pichu, sort_dist_acc_pikachu, belong_acc_pichu, belong_acc_pikachu)


# check if the point is a pichu class och pikachu class
def check_class(belong_pic, belong_pik, word):
    len_pichu = len(belong_pic)
    len_pikachu = len(belong_pik)
    print(f"Number of Pichu: {len_pichu}")                            # print for double check
    print(f"Number of Pikachu: {len_pikachu}")                        # print for double check

    if len_pichu > len_pikachu:
        print(f"{word} belongs to class Pichu\n")
    elif len_pichu == len_pikachu:
        print(f"50 - 50 for class Pichu and Pikachu \n")
    else:
        print(f"{word} belongs to class Pikachu\n")


check_class(belong_pichu, belong_pikachu, "The 5 points for test (lab2 step 2)")
check_class(belong_acc_pichu, belong_acc_pikachu, "The accuracy test points")


# calculates the accuracy
def calculate_accuracy(num_pikachu, num_pichu):
    accuracy = (len(num_pikachu) + len(num_pichu))/10
    print(f"The accuracy is {accuracy}")


calculate_accuracy(belong_acc_pikachu, belong_acc_pichu)


# lists in width and height for pichu and pikachu for plot
pichu_width = [el[0][0] for el in pichu_sort]
pichu_height = [el[0][1] for el in pichu_sort]
pikachu_width = [el[0][0] for el in pikachu_sort]
pikachu_height = [el[0][1] for el in pikachu_sort]

# for accuracy plot
pichu_acc_width = [el[0][0] for el in accuracy_pichu]
pichu_acc_height = [el[0][1] for el in accuracy_pichu]
pikachu_acc_width = [el[0][0] for el in accuracy_pikachu]
pikachu_acc_height = [el[0][1] for el in accuracy_pikachu]
test_acc_pichu_width = [el[0][0] for el in test_accurracy_pichu]
test_acc_pichu_height = [el[0][1] for el in test_accurracy_pichu]
test_acc_pikachu_width = [el[0][0] for el in test_accurracy_pikachu]
test_acc_pikachu_height = [el[0][1] for el in test_accurracy_pikachu]


# plot of Pichu and Pikachu including Test points
# for the part 1 and 2 in the basic task
plt.figure(1)
plt.title("Test_points")
plt.xlabel("width")
plt.ylabel("height")
plt.xlim(5, 40)     # cut the axis in x, the same for y
plt.ylim(15, 60)
plt.plot(pichu_width,pichu_height,'g.',label="Pichu")
plt.plot(pikachu_width, pikachu_height,'r.', label="Pikachu")
plt.plot(test_data_width, test_data_height, 'bo', label="Test points")
plt.plot()
plt.legend()

# for accuracy print
plt.figure(2)
plt.title("Accuracy")
plt.xlabel("width")
plt.ylabel("height")
plt.xlim(5, 40)     # cut the axis in x, the same for y
plt.ylim(15, 60)
plt.plot(pichu_acc_width, pichu_acc_height, 'g.', label="acc_pichu")
plt.plot(pikachu_acc_width, pikachu_acc_height, 'r.', label="acc_pikachu")
plt.plot(test_acc_pichu_width, test_acc_pichu_height, 'ko', label="test_acc_pichu")
plt.plot(test_acc_pikachu_width, test_acc_pikachu_height, 'bo', label="test_acc_pikachu")
plt.plot()
plt.legend()
plt.show()

