import math

def prime_numbers(n):
    if n == 0:
        return []
    elif n == 1:
        return [2]
    prems = [2,3]
    compt =3
    while len(prems) <=n-1:
        compt+=1
        addable = False
        for prem in prems:
            if prem <= math.sqrt(compt):
                if not (compt % prem ==0):
                    addable = True
                else:
                    addable = False
                    break
            else: break
        if addable:
            prems.append(compt)
    return prems

def is_prime(n):
    if n == 2 or n == 3:
        return True
    prems = [2,3]
    compt =3
    while compt <=n:
        compt+=1
        addable = False
        for prem in prems:
            if prem <= math.sqrt(compt):
                if not(compt % prem ==0):
                    addable = True
                else:
                    addable = False
                    break
            else: break
        if addable:
            prems.append(compt)
            if n == compt:
                return True
    return False

def map(f ,list : list):
    newList = []
    for elem in list:
        newList.append(f(elem))
    return newList

def filter(f,list : list):
    newList = []
    for elem in list:
        if f(elem):
            newList.append(elem)
    return newList

def reduce(f,list : list ):
    number = list[0]
    for i in range(1,len(list)):
        number = f(number,list[i])
    return number

def insert(list, n):
    for i,elem in enumerate(list):
        if i == 0 and n < elem:
            list = [n] + list
            return None
        
        elif list[i-1] <= n and n < elem:
            list = list[:i] + [n] + list[i:]
            return None
    list = list + [n]

def insert_ex(n,list):
    final = []
    for i in list:
        actuel = list[i]
        precedent = list[i-1]
        if i == 0 and n < actuel:
            final.append(n)
        elif precedent < n and n <= actuel:
            final.append(n)
        final.append(actuel)
    
    if list[len(list)-1]<n:
        final.append(n)
    list = final
    

print(insert_ex(20,range(3)))