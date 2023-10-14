user_input = input("Enter string. =>")
print("Inputed string:",user_input)

'''rev_word = reversed(user_input)

for letter in rev_word:
    print (letter)'''

#why i cannot use reversed for while loop :(
i = len(user_input) - 1
while i >= 0:
    print(user_input[i])
    i -= 1