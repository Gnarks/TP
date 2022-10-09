dic = []
with open("words.txt") as file:
    for line in file:
        dic.append(line.strip())

        
def belongs_to_dictionary(word):
    if word in dic:
        return True
    return False

def ask_word_dictionary():
    word = input("enter a word plz: ")
    while not belongs_to_dictionary(word):
        word = input("enter another word plz: ")
    return word

def ask_letter(tried_letters):
    letter = input("enter a letter plz: ")
    while letter in tried_letters:
        letter = input("enter another letter plz: ")
    return letter