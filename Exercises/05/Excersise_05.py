"""
Encryption
Let the user input a word and:
  a) encrypt the message by replacing each letter with the next letter.
     If the letter is in the end of the alphabet, use the first letter instead.
     e.g. in Swedish: "höst" $\rightarrow$ "iatu"
  b) decrypt the message
  c) let the user choose either encryption or decryption.
"""
import string

# strings of alfabeth UPPER and LOWER
alfabeth_lowercase = string.ascii_lowercase+"åäö"  # a - ö
alfabeth_uppercase = string.ascii_uppercase+"ÅÄÖ"  # A - Ö

"""
word = list(input("Enter a single word: "))

# a) encrypt
pos = 0
encrypted_word = ""

# find char and change pos one step forward to get encrypted char
for w in word:
    if w.isupper():
        for pos, char in enumerate(alfabeth_uppercase):
            if char == w:
                pos += 1
                new_w = alfabeth_uppercase[pos]
                encrypted_word += new_w
    elif w.islower():
        for pos, char in enumerate(alfabeth_lowercase):
            if char == w:
                pos += 1
                new_w = alfabeth_lowercase[pos]
                encrypted_word += new_w

print(encrypted_word)
"""
"""
# b) decrypt
decrypted_word = ""

# find char and change pos one step backward to get decrypted char
for letter in encrypted_word:
    if letter.isupper():
        for pos, char in enumerate(alfabeth_uppercase):
            if char == letter:
                pos -= 1
                rev_letter = alfabeth_uppercase[pos]
                decrypted_word += rev_letter
    elif letter.islower():
        for pos, char in enumerate(alfabeth_lowercase):
            if char == letter:
                pos -= 1
                rev_letter = alfabeth_lowercase[pos]
                decrypted_word += rev_letter

print(decrypted_word)
"""
# c) let the user choose decrypt or encrypt

word = input("Enter a single word: ")

if word.isalpha():
    choice = input("Enter A for Encrypt word or B for Decrypt word: ")

    pos = 0
    encrypted_word = ""

    # find char and change pos one step forward to get encrypted char
    for w in word:
        if w.isupper():
            for pos, char in enumerate(alfabeth_uppercase):
                if char == w:
                    pos += 1
                    new_w = alfabeth_uppercase[pos]
                    encrypted_word += new_w
        elif w.islower():
            for pos, char in enumerate(alfabeth_lowercase):
                if char == w:
                    pos += 1
                    new_w = alfabeth_lowercase[pos]
                    encrypted_word += new_w
    if choice == "A" or choice == "a":
        print(f"Encrypted: {encrypted_word}")


    decrypted_word = ""

    # find char and change pos one step backward to get decrypted char
    for letter in encrypted_word:
        if letter.isupper():
            for pos, char in enumerate(alfabeth_uppercase):
                if char == letter:
                    pos -= 1
                    rev_letter = alfabeth_uppercase[pos]
                    decrypted_word += rev_letter
        elif letter.islower():
            for pos, char in enumerate(alfabeth_lowercase):
                if char == letter:
                    pos -= 1
                    rev_letter = alfabeth_lowercase[pos]
                    decrypted_word += rev_letter

    if choice == "B" or choice == "b":
        print(f"Decrypted: {decrypted_word}")

else:
    print("Only alfanumeric letters")
    