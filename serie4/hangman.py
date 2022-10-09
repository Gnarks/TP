from userInput import *
tried_letters = []
daWord = "aah"

for i in range(11):
    p2_word = input("player 2, please choose a word:")
    while not belongs_to_dictionary(p2_word):
        p2_word = input("player 2, please choose a word in the dictionary :")
    if p2_word == daWord:
        print("GG")
        score = daWord.__len__() + i - tried_letters.__len__()
        break
    print(f"Turn(s) left(s): {10 -i}\n Letter(s) tried :")
    for letter in tried_letters:
        print(f"{letter}",end="")
    print()
    for char in daWord:
        if char in tried_letters:
            print(f"{char}", end='')
        else:
            print("*",end="")
    print()
    p1_char =input("player 1, please choose a character:")
    while p1_char in tried_letters:
        p1_char = input("player 1,please choos another character:")
    tried_letters.append(p1_char)
    