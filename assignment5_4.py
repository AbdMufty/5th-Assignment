while True:
    sentence = input("Please enter a string: ")
    
    remove_chr = ":,.;!?"
    
    if sentence.lower() == "done":
        print("Bye!!!")
        break
    
    pre_trans_sentence = str.maketrans('', '', remove_chr)
    post_trans_sentence = sentence.translate(pre_trans_sentence)
    
    print(post_trans_sentence.upper())