"""
National test
Read in the file NPvt19Ma2A.txt and NPvt19Ma2C.txt in Python. 
Use matplotlib to plot pie charts for each grade categories in each file.
"""

path_2a = "C:/Users/trull/Documents/GitHub/PythonProgrammering-MarieJonsson/Code-Along/Files/NPvt19Ma2A.txt"
path_2c = "C:/Users/trull/Documents/GitHub/PythonProgrammering-MarieJonsson/Code-Along/Files/NPvt19Ma2C.txt"
with open(path_2a, "r") as f2a, open(path_2c, "r") as  f2c:
    print(f2a.readlines())
    print(f2c.readlines())