"""
Test results
Read in the file test_result.txt in Python.
  a)   Print out the text in the terminal
  b)   Create new rows in the same file and write the people and 
       their corresponding scores in alphabetical order.
  c)   Create additional rows in the same file and sort the people 
       after their grades. The grade limits are: 

F < 20
E: 20-29
D: 30-39
C: 40-49
B: 50-59
A: 60-70
"""
path = "C:/Users/trull/Documents/GitHub/PythonProgrammering-MarieJonsson/Code-Along/Files/test_result.txt"

grade_F = []
grade_E = []
grade_D = []
grade_C = []
grade_B = []
grade_A = []


def set_grade(grade, text):
    grade.append(text)


def add_to_file(grade, grade_name):
    with open(path,"a", encoding= "utf-8") as f3:
        f3.write(f"\n\n{grade_name}\n")
        for x in grade:
            f3.write(f"{x}\n")


with open(path, "r", encoding="utf-8") as f1, open(path, "a", encoding="utf-8") as f2:
    texts = [text.strip(" \n") for text in f1.readlines()]
    print(f"Text in terminal from file: {texts}")                       # a) print text in terminal
    texts = sorted(texts)               # sortered

    f2.write("\n\nSorted alphabetical order\n")
    for text in texts:                  # b) In alphabetical order to file
        f2.write(f"{text}\n")

    for text in texts:
        t_split = text.split(" ")
        t2 = int(t_split[-1])

        if t2 < 20:
            set_grade(grade_F, text)

        elif t2 <= 29:
            set_grade(grade_E, text)

        elif t2 <= 39:
            set_grade(grade_D, text)

        elif t2 <= 49:
            set_grade(grade_C, text)

        elif t2 <= 59:
            set_grade(grade_B, text)

        elif t2 <= 70:
            set_grade(grade_A, text)


add_to_file(grade_A, "Grade A")
add_to_file(grade_B, "Grade B")
add_to_file(grade_C, "Grade C")
add_to_file(grade_D, "Grade D")
add_to_file(grade_E, "Grade E")
add_to_file(grade_F, "Grade F")

