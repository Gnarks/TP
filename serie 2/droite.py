from cmath import sqrt

def droite_equ(p1,p2):
    """fonction qui donne la droite qui passe entre les deux points donnés en arguments

    Args:
        p1 (float tuple): (x1,y1)
        p2 (float tuple): (x2,y2)

    Returns:
        tuple:(a,b,c) de la droite d'équation ax+by+c
    """
    if p1 == p2: # check si les deux points sont les mêmes
        return None
    (x1,y1) = p1
    (x2,y2) = p2
    if(x1==x2):# cas d'une droite verticale donc b = 0
        return(-1,0,-x1)
    a = (y2-y1)/(x2-x1) # calcul de la pente
    c = y1-a*x1 # calcul du l'OàO
    return(-a,1,c)

def appartient(d,p):
    """vérifie si le point p appartient à la droite d

    Args:
        d (float tuple): (a,b,c)
        p (float tuple): (x,y)

    Returns:
        bool: vrai ou faux en fonction de si oui ou non le point appartient à la droite
    """
    (x,y) = p
    a,b,c = d
    return x*a +b*y == c

def paralleles(d1, d2):
    """vérifie si les droites d1 et d2 sont parralleles

    Args:
        d1 (_type_): (a1,b1,c1)
        d2 (_type_): (a2,b2,c1)

    Returns:
        bool: true ou false
    """
    a1,b1,c1 = d1
    a2,b2,c2 = d2
    if((b1!=0 and b2!=0) and a1/b1 == a2/b2):
        return True
    return b1 == 0 and b2 == 0

def intersection(d1,d2):
    if d1 == d2:
        return None# vérifie si les droites ne sont pas confondues
    a1,b1,c1 = d1
    a2,b2,c2 = d2
    a1 = a1/b1
    a2 = a2/b2
    c1 = c1/b1
    c2 = c2/b2# calcul pour repasser en y = mx+p
    if a2-a1 == 0:
        return None
    x = -(c2-c1)/(a2-a1)
    y = a1*x + c1
    return (-x,y)


def droite_normale(d,p):
    (a1,b1,c1) = d
    if b1 == 0:
        return(0,1,-p[1])
    elif a1==0:
        return(1,0,-p[0])
    b2 = -b1
    a2 = (b2*b1)/a1
    c2 = -a2*p[0]-b1*p[1]
    return(a2,-b2,-c2)


def symetrie_orthogonale(d,p):
    if appartient(d,p):
        return p
    (x,y) = p
    normale = droite_normale(d,p)
    (xo,yo) = intersection(d, normale)
    return 2*xo -x, yo*2 -y


def distance_droite_point(d, p):
    if appartient(d,p):
        return 0.0
    (x,y) = p
    a,b,c = d
    return abs(a+b+c)/sqrt(a**2 + b**2)

