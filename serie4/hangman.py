from userInput import *
from hangmantui import *
tried_letters = []
print_word = ""
i = 10

clear()
word = ask_word_dictionary()
dif_letters = 0
clear()

for char in word:
    if not (word.count(char) >0):
        dif_letters+=1
    
while i >0:
    hangman(i)
    letter = ask_letter(tried_letters)
    if not (letter in word):
        i-=1
    tried_letters.append(letter)

    for char in word:
        if char in tried_letters:
            print_word += char
        else:
            print_word += "*"
    clear()
    for letter in tried_letters:
        print(letter,end=" ")
    print(f"\nmot : {print_word}")
    if not ("*" in print_word):
        score = dif_letters + i - len(tried_letters)
        break
    print_word = ""