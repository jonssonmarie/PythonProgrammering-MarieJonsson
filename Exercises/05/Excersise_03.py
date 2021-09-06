"""
Palindrome
A palindrome is a sequence of characters that is the same, 
when read forward as backwards (ignoring spaces). 
For example:
"Anna" is a palindrome
"Ni talar bra latin"
bjkjb
Let the user input a sequence of characters and check if it is a palindrome.
"""

sentence = input("Enter a sentence to check if palindrome: ")
sentence.replace(" ", "")  # tar bort whitespace mellan orden

lst = [] 

# loop for each letter in sentence and append to lst
for i in sentence:
    if i.isupper():             # change to lowercase
        lst.append(i.lower())
    if i.islower():             # remain lower case
        lst.append(i)
    if not i.isalpha():         # skip if not alfanumeric
        continue

#print(lst)   
#  
# check if letters are the same counting from first pos and last pos, stepping each way
if lst == lst[::-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")

