"""
Counting letters
Let the user input a word:
  a) print out the number of letters in the word.
  b) print out the number of uppercase and lowercase letters of the word
"""

import re

word = input("Enter a single word: ")

# a
num_letters = len(word)
print(f"The number of letters in {word} is {num_letters}")

# b  Flera sätt
## UPPERCASE
count_uppercase = len(re.findall(r'[A-Z]', word)) 
print(f"Number of uppcase A-Z: {count_uppercase}")  # för A-Z, ej ÅÄÖ

count_uppercase2 = len([letter for letter in word if letter.isupper()])
print(f"Number of uppcase A-Ö: {count_uppercase2}")  # funkar även för ÅÄÖ

count_uppercase3 = sum(1 for letter in word if letter.isupper())
print(f"Number of uppcase A-Ö: {count_uppercase3}")  # funkar även för ÅÄÖ

# LOWERCASE
count_lowercase = len(re.findall(r'[a-z]', word)) # för a -z, ej åäö
print(f"Number of lowercase a-z: {count_lowercase}") 

count_lowercase1 = len([letter for letter in word if letter.islower()])
print(f"Number of lowercas a-ö: {count_lowercase1}")  # funkar även för åäö

count_lowercase2 = sum(1 for letter in word if letter.islower())
print(f"Number of lowercas a-ö: {count_lowercase2}")  # funkar även för åäö
