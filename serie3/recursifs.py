def somme1(n):
    if n == 0:
        return 0
    else:
        somme1(n-1)+n # reroutne None et non la somme


def somme2(n):
    if n == 0:
        return 0
    else:
        return somme2(n)+n # ne décrémente jamais n donc appelle la fonction à l'infini


def somme3(n):
    if n == 0:
        return 0
    else:
        return n+somme3(n-1) # est correct 


def somme4(n):
    if n == 0:
        res = 0
    else:
        somme4(n)+n
        return res # on ne donne pas de valeur à res avant de le return 


def somme5(n):
    return somme5(n-1)+n # n'a pas de condition d'arret