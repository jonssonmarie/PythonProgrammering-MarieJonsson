"""
National test
Read in the file NPvt19Ma2A.txt and NPvt19Ma2C.txt in Python. 
Use matplotlib to plot pie charts for each grade categories in each file.
"Files/NPvt19Ma2A.txt" 
"Files/NPvt19Ma2C.txt"
"""
import matplotlib.pyplot as plt

list_2a = []
list_2c = []

path_2a = "C:/Users/trull/Documents/GitHub/PythonProgrammering-MarieJonsson/Code-Along/Files/NPvt19Ma2A.txt"
path_2c = "C:/Users/trull/Documents/GitHub/PythonProgrammering-MarieJonsson/Code-Along/Files/NPvt19Ma2C.txt"

with open(path_2a, "r") as f2a, open(path_2c, "r") as  f2c:
    data_2a = f2a.readlines()
    data_2c = f2c.readlines()
    
    def clean_text(datan, a_list):
        for data in datan:
            d = (data.strip(" \n").strip("%"))
            d_split = d.split(" ")
            a_list.append(d_split)
            

    clean_text(data_2a, list_2a)
    clean_text(data_2c, list_2c)
   
   
    grade_2a = []
    percentage_2a = []
    grade_2c = []
    percentage_2c = []


    def get_to_list(list_x, grade_x, perc_x):
        for x in list_x:
            grade_x.append(x[0])
            perc_x.append(x[1])
    
    get_to_list(list_2a, grade_2a, percentage_2a)
    get_to_list(list_2c, grade_2c, percentage_2c)


    # subplot
    plt.figure()
    plt.subplot(1,2,1)
    plt.title("NPvt19Ma2A")
    plt.pie(percentage_2a,labels=grade_2a)

    plt.subplot(1,2,2)
    plt.title("NPvt19Ma2C")
    plt.pie(percentage_2c,labels=grade_2c)
 