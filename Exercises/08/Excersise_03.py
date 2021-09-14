"""
National test
Read in the file NPvt19Ma2A.txt and NPvt19Ma2C.txt in Python. 
Use matplotlib to plot pie charts for each grade categories in each file.
"Files/NPvt19Ma2A.txt" 
"Files/NPvt19Ma2C.txt"
"""

data_collected = []
data_alpha = []

path_2a = "C:/Users/trull/Documents/GitHub/PythonProgrammering-MarieJonsson/Code-Along/Files/NPvt19Ma2A.txt"
path_2c = "C:/Users/trull/Documents/GitHub/PythonProgrammering-MarieJonsson/Code-Along/Files/NPvt19Ma2C.txt"
with open(path_2a, "r") as f2a, open(path_2c, "r") as  f2c:
    data_2a = f2a.readlines()
    data_2c = f2c.readlines()
    #print(data_2c)
    """
    läs in
    rensa data \n och %
    lägg i listor en med bokstäver och en med siffror
    """
    def clean_text(datan):
        for data in datan:
            d = (data.strip(" \n").strip("%"))
            d_split = d.split(" ")
            data_collected.append(d_split[1])
            data_alpha.append(d_split[0])
            print(d_split)


    
    clean_text(data_2a)
    clean_text(data_2c)

    print(data_collected)
    print(data_alpha)