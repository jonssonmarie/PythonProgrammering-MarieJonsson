
import matplotlib.pyplot as plt
import math
import random as rnd

# paths to files
path = "../files/morse.txt"
pichu_path = "..files/pichu.txt"
pikachu_path = "..files/pikachu.txt"
test_points_path = "..files/test_points.txt"

# open and read files
with open(pichu_path, 'r') as pichu, open(pikachu_path, 'r') as pikachu, open(test_points_path, 'r') as test_point:
    pichu_points = pichu.readlines()[1:]
    pikachu_points = pikachu.readlines()[1:]
    test_points = test_point.readlines()


while True:  #               FUNKAR INTE FÖR MIMUS ÄNNU  -------------------------
    user = input("Skriv in en testpunkt x,y och se den klass den tillhör: ")
    try:
        user_data = []      #list för user_data
        coord = user.split(",")

        if len(coord) <= 2 :
            for c in coord:
                cc = float(c)
                if cc <= 0.0:
                    print("Vänligen använd positiva koordinater")
                    break
                else:
                    point = float(cc)
                    user_data.append(point)
                    continue
            break
        else:
            print("Vänligen skriv 1 koordinat med siffor och delad med komma tex: 29.05678, 36.578687")
            continue
    except:
        print("Vänligen skriv 1 koordinat med siffor och delad med komma tex: 29.05678, 36.578687")
        continue


test_data = []          # for testdata and input data maybe
pichu_sort = []
pikachu_sort =[]


# Sort and clean data from Pichu and Pikachu
def sort_data(data_files, name, folder):
    for file in data_files:
        if data_files != test_points:
            l_clean = file.replace("(", "").replace(")", "").replace("\n", "").replace(" ", "").replace("cm", "")
            l_split = l_clean.split(",")
            width = float(l_split[0])
            height = float(l_split[1])
            val = [[width, height], name]
            folder.append(val)
        else:
            l_split = file.split(",")
            for l in l_split:
                l_clean = l.replace("(", "").replace(")", "").replace(" ", "")
                l = float(l_clean)
                test_data.append(l)


sort_data(test_points, "", "")
sort_data(pichu_points, "pichu", pichu_sort)
sort_data(pikachu_points, "pikachu", pikachu_sort)


# randomly chosen traning data and test data
training_data_pichu = rnd.sample(pichu_sort, 45)
training_data_pikachu = rnd.sample(pikachu_sort, 45)
test_data_pichu = rnd.sample(pichu_sort, 5)
test_data_pikachu = rnd.sample(pikachu_sort, 5)

# Kidnappar för att testa accuracy ! -----------------------------------------------------------------------
pichu_sort = training_data_pichu
pikachu_sort = training_data_pikachu
#test_data = user_data   # debugg till bara testa test_datan - > sätt # framför


# Test points data sorted by width and height
test_data_width = test_data[0:len(test_data):2]
test_data_height = test_data[1:len(test_data):2]
test_data_w_h = []


def width_height_test_data(width_test, height_test):
    for (width, height) in zip(width_test, height_test):
        val = [width, height]
        test_data_w_h.append(val)


width_height_test_data(test_data_width, test_data_height)


all_distance = []   # obsolet ?
all_coord = []
all_tp = []
distance_pichu = []
distance_pikachu = []


def euclidean_distance(data_p, data_test, folder):
    for d in data_p:
        d_p = d[0]
        for test in data_test:
            dist = math.sqrt(math.pow((test[0]-d_p[0]), 2) + (math.pow((test[1]-d_p[1]), 2)))
            coord = [d, test, dist]
            tp_dist = [dist, test]
            all_dist = [dist, data_p[0][1]]
            all_distance.append(all_dist)  # obsolet ?
            folder.append(all_dist)
            all_coord.append(coord)
            all_tp.append(tp_dist)


euclidean_distance(pichu_sort, test_data_w_h, distance_pichu)
euclidean_distance(pikachu_sort, test_data_w_h, distance_pikachu)


def sort_for_user_data_one(distance_1, distance_2):
    sort_dist_1 = sorted(distance_1)[0:1]
    sort_dist_2 = sorted(distance_2)[0:1]
    if sort_dist_1[0][0] < sort_dist_2[0][0]:
        print(f"Only for test - Testpunkten {user_data} tillhör klass Pichu")
    else:
        print(f"Only for test - Testpunkten {user_data} tillhör klass Pikachu")


sort_for_user_data_one(distance_pichu, distance_pikachu)


sort_dist_1 = sorted(distance_pichu)[0:5]
sort_dist_2 = sorted(distance_pikachu)[0:5]

# zip two lists elem by elem and then compare and measure how many pichu vs pikachu there is
belong_pichu = []
belong_pikachu = []


def sort_for_user_data_five(distance_1, distance_2):
    comp_list = []
    for (dist1, dist2) in zip(distance_1, distance_2):
        val = [dist1, dist2]
        comp_list.append(val)

    for elem in comp_list:
        if elem[0][0] < elem[1][0]:
            belong_pichu.append("1")
        else:
            belong_pikachu.append("1")


sort_for_user_data_five(sort_dist_1, sort_dist_2)


def check_class(belong_pic,belong_pik):
    len_pichu = len(belong_pic)
    len_pikachu = len(belong_pik)
    print("len_pichu",len_pichu)                            # print för dubbelkoll
    print("len_pikachu", len_pikachu)                       # print för dubbelkoll

    if len_pichu > len_pikachu:
        print(f"Testpunkten {user_data} tillhör klass Pichu")
    else:
        print(f"Testpunkten {user_data} tillhör klass Pikachu")


check_class(belong_pichu, belong_pikachu)


# lists in width and height for pichu and pikachu for plot
pichu_width = [el[0][0] for el in pichu_sort]
pichu_height = [el[0][1] for el in pichu_sort]
pikachu_width = [el[0][0] for el in pikachu_sort]
pikachu_height = [el[0][1] for el in pikachu_sort]


# plot of Pichu and Pikachu including Test points
"""
begränsa hur stora punkter som får läggas in.
Pichu width 15 - 22 height 25 - 35
Pikachu width 18 - 29  height 35 - 45
"""
plt.figure(1)
plt.title("Test_points")
plt.xlabel("width")
plt.ylabel("height")
plt.xlim(5, 40)     # cut the axis in x, the same for y
plt.ylim(15, 60)
plt.plot(pichu_width,pichu_height,'gx',label="Pichu")
plt.plot(pikachu_width, pikachu_height,'r.', label="Pikachu")
plt.plot(test_data_width, test_data_height, 'bo', label="Test points")
plt.plot()
plt.legend()
#plt.show()



def calculate_accuracy():
    """
    accuracy = (TP + TN)/ Total
    Här har vi låtit Pikachu vara positiv och Pichu vara "icke-Pikachu" dvs negativ.
    """

calculate_accuracy()

