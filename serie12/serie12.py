def grandBord(w):
    bord =0
    for i in range(1,len(w)):
        if w[:i] == w[-i:]:
            bord = i
    return w[:bord] if bord > 0 else None

def intersection(v,w):
    inter = ""
    for i in range(len(v)):
        for j in range(len(w)):
            a = i
            b = j
            temp =""
            while a < len(v) and b < len(w) and v[a] == w[b]:
                temp+= v[a]
                a+=1
                b+=1
            if len(temp) > len(inter):
                inter = temp
    return inter if len(inter)>1 else None

def anagrammes(v,w):
    if len(v) != len(w):
        return False
    for char in w:
        if char not in v:
            return False
    return True
    
    
def palindrome(w):
    if w == reversed(w):
        return True
    return False

def chiffrement_vigenere(txt,mot):
    final = ""
    for i in range(len(txt)):
        plus = ord(mot[i%len(mot)])-65   
        change = (ord(txt[i])-97 +plus)%26
        final+= chr(change+65)
    return final

def dechiffrement_vigenere(txt,mot):
    final = ""
    for i in range(len(txt)):
        moins = ord(mot[i%len(mot)])-65
        change = (ord(txt[i])-97 -moins)%26
        final+= chr(change+65)
    return final.lower()

def is_sym(mat_img):
    hori = True
    verti = True
    for i in range(len(mat_img)):
        for j in range(len(mat_img[i])):
            if mat_img[i][j] != mat_img[i][len(mat_img[i])-j-1]:
                hori = False
            if mat_img[i][j] != mat_img[len(mat_img)-i-1][j]:
                verti = False
    return hori,verti

vigenere = "yzadgqxqmmtpxazvblxitapsgmnedinexsikallqotgvrp"
#print(dechiffrement_vigenere(vigenere,"ALGORITHME"))

#print(intersection("programme","grammaire"))
#print(intersection("cardinalite","ordinateur"))

