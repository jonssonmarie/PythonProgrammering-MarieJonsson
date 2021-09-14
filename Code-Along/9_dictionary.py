"""
Föreläsning
9.00 -11.45
   - ledningsgrupp - tack för igår
   - set - plocka ut unika värden från listan ex: 1,2,3,3,3, 4,5,5 -> 1,2,3,4,5
   - dictionary

Stuga
13.15 -16.00
"""

# Dictionary
"""
 - key:value pair
"""

"""
person = dict(
    name = "Kokchun",
    age = 30.4,
    work = "Teacher",
    interests = ["math", "programming", "python", "yoga"],
    likes_job = True )

# printa respektive value från den key som anges
print(f"personal dictionary {person}")
print(f"Personens namn är {person['name']}")
print(f"Personens ålder är {person['age']} år")

# loop genom alla intressen
for interest in person["interests"]:
    print(f"{person['name']} likes {interest}")

"""


"""
words = {
    "data structure": "means of storing and organizing data",
    "lambda": "anonymous function",
    "class" : "blueprint for objects"
        }

print("Vi ska lära oss dessa ord:")
for key in words:
    print(key)
    
print(f"\n\nGlosa {'':<15} Betydelse")
for key, value in words.items():
    print(f"{key:<21} {value}")   # :< 15 förflyttar till höger
    #print("key: ",key)
    #print("value: ",value)
"""


"""
# f<10, E:10, D:20, C:30, B:40, A:50

grade_limits = {}
grades = list("ABCDEF")
print(grades)

# create a new value to a befintlig key
words["lambda"] = "an anonymous function"  # overwrites previous value
words["regression"] = "find a function that best fits observed data"  # overwrites previous value

print(words)

for i, grade in enumerate(grades[::-1]):
    grade_limits[grade] = i*10

grade_limits["F"] = "<10"
print(grade_limits)
"""


"""
Dictionary comprehension
"""

import random as rnd
grade_limits = {grade:i *10 for i, grade in enumerate("FEDCBA")}

print(grade_limits)

def generate_scores(number_scores):
    rnd.seed(42)   # seed ger samma tal pga talet 42 
    scores = [rnd.randint(0,60) for _ in range(number_scores)]
    return scores

print(f"Student scores: {generate_scores(20)}")

scores = generate_scores(20)

grade_count = {key: 0 for key in grade_limits}
print(grade_count)


for score in scores:
    for grade, limit in grade_limits.items():
        if limit <= score < limit+10:
            grade_count[grade] += 1
print(f" Grade count {grade_count}")






