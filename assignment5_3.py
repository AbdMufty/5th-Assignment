sentence = input("please rnter a string: ")
up_letter = 0
low_letter = 0
number = 0
sp_chr = 0

for letter in sentence:
    if letter.isupper():
        up_letter += 1
    elif letter.islower():
        low_letter += 1
    elif letter.isnumeric():
        number += 1
    else:
        sp_chr += 1

print(f"Uppercase letter: {up_letter}\nLowercase letter: {low_letter}\nNumbers: {number}\nOthers characters: {sp_chr}")