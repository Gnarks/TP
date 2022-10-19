from math import sqrt

"""def oui(lelist):
    res = []
    for i in range(len(lelist)):
        res.append(sum(lelist[:i+1]))
    return res

lalist = [1,2,3]
print(oui(lalist))"""

"""A = [5,3,66,32,16,24,6,5,96]
print(list(filter(lambda x: x%10==6,list(map(lambda x:x**2,A)))))
"""

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
            print(prem, compt,prem <= sqrt(compt), not (compt%prem ==0))
            if prem <= sqrt(compt):
                if not(compt % prem ==0):
                    addable = True
                else: 
                    addable = False
                    break
            else: break
        if addable:
            prems.append(compt)
            print("added", compt)

    return prems


print(prime_numbers(12))