while True:
    inp_word = input("Input 2 words seperated by a space\n==> ")
    if inp_word == "done" or len(inp_word) == 0:
        print("Bye!!!")
        break

    sepereted_words = sorted(inp_word.split())
    
    if any(word.isdigit() for word in sepereted_words):
        print("Please enter 2 valid words.")
        continue

    if len(sepereted_words) == 2:
        word_1, word_2 = sepereted_words[0], sepereted_words[1]
        print(f"{word_1} comes first")
    else:
         print("Please enter 2 words.")
