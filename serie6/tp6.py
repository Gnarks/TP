import random

def creerEnchevetrements(bag,i,max_ench):
    max_ench = random.randrange(1,max_ench)
    bag_copy = [j for j in bag if j != i]
    return [(j,i) for j in random.choices(bag_copy,k=max_ench)]
        
def creerMikado(bag):
    list_ench = []
    for i in bag:
        list_ench += creerEnchevetrements(bag,i,len(bag))
    return list_ench

def peutRetirer(i,bag,jeu):
    for ench in jeu:
        if ench[1] == i:
            return False
    return True
    
def quelOrdre(bag, jeu):
    if len(bag) == 1:
        return [bag[0]]
    for i in bag:
        if peutRetirer(i,bag,jeu):
            nextBag = [j for j in bag if j != i]
            nextJeu = list(filter(lambda couple: i not in couple,jeu))
            return [i] + quelOrdre(nextBag,nextJeu)
    return None

def estJouable(bag,jeu):
    if len(jeu) ==0:
        return True
    for i in bag:
        if peutRetirer(i,bag,jeu):
            nextBag = [j for j in bag if j != i]
            nextJeu = list(filter(lambda couple: i not in couple,jeu))
            #nextJeu = [ench for ench in jeu if ench[1] != i]
            return estJouable(nextBag,nextJeu)
    return False

bag = [1,2,3,4]
myJeu= [(3,1),(3,4),(1,2),(4,2)]
print(estJouable(bag,myJeu))
print(quelOrdre(bag,myJeu))