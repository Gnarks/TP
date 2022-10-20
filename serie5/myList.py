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

def insert(arg_list, n):
    for i,elem in enumerate(arg_list):
        if i == 0 and n < elem:
            arg_list = [n] + arg_list
            return None
        
        elif arg_list[i-1] <= n and n < elem:
            arg_list = arg_list[:i] + [n] + arg_list[i:]
            return None
    arg_list = arg_list + [n]
    
    
def produit_matriciel(a,b):
    if a == [] and b == []:
        return []
    if not (len(a) == len(b[0])):
        return None
    c= []
    for i in range(len(a)):
        c.append([])
    for i in range(len(a)):
        line = []
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(b)):
                sum += a[i][k] * b[k][j]
            line.append(sum)
        c.append(line)
    return c

print(is_prime(95647806479275528135733781266203904794419563064407))