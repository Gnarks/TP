from uturtle import *

def arbre(t, x, a, n):
    moveForward(t,x)
    turnLeft(t,a)
    branche(t,x*(3/4),a,n)
    turnRight(t,a*2)
    branche(t,x*(3/4),a,n)
    turnLeft(t,a)
    moveBackward(t,x)

def branche(t,x,a,n):
    if n == 1:
        moveForward(t,x)
        moveBackward(t,x)
        return

    moveForward(t,x)
    turnLeft(t,a)
    branche(t, x*(3/4), a*(3/4), n-1)
    turnRight(t,a*2)
    branche(t, x*(3/4), a*(3/4), n-1)
    turnLeft(t,a)
    moveBackward(t,x)


def koch(t,x,seuil):
    if(x<seuil):
        moveForward(t,x)
        return
    koch(t, x/3, seuil)
    turnLeft(t,60)
    koch(t, x/3, seuil)
    turnRight(t,120)
    koch(t, x/3, seuil)
    turnLeft(t,60)
    koch(t, x/3, seuil)

def flocon(t,x,seuil,nbr_cotes):
    cote_flocon(t, x, seuil, nbr_cotes,nbr_cotes)

def cote_flocon(t,x,seuil,nbr_cotes,n):
    if (n==0):
        return
    koch(t, x, seuil)
    turnLeft(t,360/nbr_cotes)
    cote_flocon(t, x, seuil, nbr_cotes, n-1)

def carre(t,x,seuil):
    if(x<seuil):
        moveForward(t,x)
        return
    carre(t, x/4, seuil)
    turnLeft(t,90)
    carre(t, x/4, seuil)
    turnRight(t,90)
    carre(t, x/4, seuil)
    turnRight(t,90)
    carre(t, x/4, seuil)    
    turnLeft(t,90)
    carre(t, x/4, seuil)

def go_to_bottom(t):
    dropPen(t)
    turnLeft(t)
    moveBackward(t,380)
    usePen(t)
    
bobby = umonsTurtle()
flocon(bobby, 45, 15,8)# je me suis permis de mettre un paramêtre pour le nombre de cotés
#carre(bobby,500,15)
go_to_bottom(bobby)
#arbre(bobby,200,30,3)
wait()