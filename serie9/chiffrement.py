import sys

def lecture(nom):
    result = ""
    with open(nom,"r") as f:
        lines = f.readlines()
        for line in lines:
            result+=line
    
    return result

def nettoyage(texte):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in texte:
        char = char.lower()
        if char in alphabet:
            result+=char
    return result            
            
def chiffrement_decalage(fichier,u):
    texte = nettoyage(lecture(fichier))
    # chr(97) = "a"
    # ord("a") = 97
    result = ""
    for char in texte:
        result += chr(ord(char)+u) if ord(char)+u >= 97 and ord(char)+u < 123 else chr(ord(char)-26+u)
    print(result)
    return result

    
def dechiffrement_decalage(fichier,u):
    texte = nettoyage(lecture(fichier))
    result = ""
    for char in texte:
        result += chr(ord(char)-u) if ord(char)-u >= 97 and ord(char)-u < 123 else chr(ord(char)+26-u)
    print(result)
    return result

def chiffrement_substitution(fichier,fichier_dico):
    texte = nettoyage(lecture(fichier))
    dico = dict()
    with open(fichier_dico,"r") as f:
        lines = f.readlines()
        for line in lines:
            key =line[0]
            value = line[2]
            dico[key] = value

    result = ""
    for char in texte:
        result+= dico.get(char,char)
    return result

def dechiffrement_substitution(fichier,fichier_dico):
    texte = nettoyage(lecture(fichier))
    dico = dict()
    with open(fichier_dico,"r") as f:
        lines = f.readlines()
        for line in lines:
            key =line[2]
            value = line[0]
            dico[key] = value
            
    result = ""
    for char in texte:
        result+= dico.get(char,char)
    return result



def decouvre_cle(text,i):
    dic_prob = {'a' : 9.42, 'b' : 1.02, 
                      'c' : 2.64, 'd' :3.39, 'e': 15.87, 'f' : 0.95, 'g': 1.04, 'h':0.77, 'i':8.41, 'j':0.89,
                      'k': 0.0, 'l' : 5.34, 'm' : 3.24, 'n': 7.15, 'o':5.14, 'p':2.86, 'q':1.06, 'r':6.46, 's':7.90, 't':7.26,'u':6.24, 'v':2.15,
                      'w': 0.0, 'x': 0.30, 'y':0.24, 'z':0.32}
    sorted_dic_prob = sorted(dic_prob.items(), key=lambda x: x[1], reverse=True)
    char_prob = dict()
    for char in text:
        if char in char_prob:
            char_prob[char] += 1/len(text)
        else:
            char_prob[char] = 1/len(text)
            
    sorted_char_prob = sorted(char_prob.items(), key=lambda x: x[1], reverse=True)
    final_dico = dict()
    for let in range(i):
        final_dico[sorted_dic_prob[let][0]] = sorted_char_prob[let][0]
    return  final_dico
    
    

if(sys.argv[1]) == "d" and ( sys.argv[2] == "d"):
    dechiffrement_decalage(sys.argv[3],int(sys.argv[4]))
if(sys.argv[1]) == "d" and ( sys.argv[2] == "c"):
    chiffrement_decalage(sys.argv[3],int(sys.argv[4]))
if(sys.argv[1]) == "s" and ( sys.argv[2] == "c"):
    chiffrement_substitution(sys.argv[3],sys.argv[4])
if(sys.argv[1]) == "s" and ( sys.argv[2] == "d"):
    dechiffrement_substitution(sys.argv[3],sys.argv[4])
if(sys.argv[1]) == "cle":
    decouvre_cle(nettoyage(lecture(sys.argv[2])),2)
