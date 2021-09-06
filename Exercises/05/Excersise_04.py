"""
Vowels
Count the number of vowels in this sentence: 
"Pure mathematics is, in its way, the poetry of logical ideas"
"""

vowels = "aeiou"  # vowels

sentence = "Pure mathematics is, in its way, the poetry of logical ideas"

# change uppercase to lowercase since vowels are lowercase
sentence_lowercase = sentence.lower()

# no need to remove comma sign since they will not trigger in for loop

count = 0   

# count number of vowels
for letter in sentence_lowercase:
    if letter in vowels:
        count +=1

print(f"The number of vowels in the sentence are: {count}")

