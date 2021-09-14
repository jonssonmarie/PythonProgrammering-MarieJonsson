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
data_alpha = []

path_2a = "Files/NPvt19Ma2A.txt" # "C:/Users/trull/Documents/GitHub/PythonProgrammering-MarieJonsson/Code-Along/Files/NPvt19Ma2A.txt"
path_2c = "Files/NPvt19Ma2C.txt" #"C:/Users/trull/Documents/GitHub/PythonProgrammering-MarieJonsson/Code-Along/Files/NPvt19Ma2C.txt"
with open(path_2a, "r") as f2a, open(path_2c, "r") as  f2c:
    data_2a = f2a.readlines()
    data_2c = f2c.readlines()
    #print(data_2c)
    """
    läs in
    rensa data \n och %
    lägg i listor en med bokstäver och en med siffror
    """
    def clean_text(datan, a_list):
        for data in datan:
            d = (data.strip(" \n").strip("%"))
            d_split = d.split(" ")
            
            a_list.append(d_split)
            data_alpha.append(d_split[0])
            print(d_split)

    clean_text(data_2a, list_2a)
    clean_text(data_2c, list_2c)
   
 
    grade_2a = []
    percentage_2a = []
    grade_2c = []
    percentage_2c = []

    #fig1, d = plt.subplot()
    for x in list_2a:
        grade_2a.append(x[0])
        percentage_2a.append(x[1])
    
    for x in list_2c:
        grade_2c.append(x[0])
        percentage_2c.append(x[1])
    
    plt.plot(grade_2a, percentage_2a)
    plt.pie(percentage_2a)
    plt.title("NPvt19Ma2A")
    plt.show()



