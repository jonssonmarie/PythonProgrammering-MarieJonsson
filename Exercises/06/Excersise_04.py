"""
Name cleaner
Create a function that takes a name as an input and:

- removes all leading and trailing blank spaces
- make capitalize the first character of each name, and make the rest lowercase
- Use your function on this list of strings:
["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "  ]
"""
lst = ["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "]
new_lst = [] # temporary empty list, also used to append to just to check name


def name_cleaner(lst):
    for l in lst:
        l = str(l).title()
        l = l.strip()
        l.join(new_lst)
        #new_lst.append(l)
        print(l)

name_cleaner(lst)
