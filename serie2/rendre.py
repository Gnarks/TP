def rendreMonnaie(prix,billets):
    b20,b10,b5,p2,p1 = billets
    given = b20*20+b10*10+b5*5+p2*2+p1
    if given < prix:
        return None
    rendre = given-prix
    rb20 = rendre // 20
    rendre= rendre % 20
    rb10 = rendre //10
    rendre= rendre %10
    rb5 = rendre //5
    rendre= rendre %5
    rp2 = rendre //2
    rendre= rendre %2
    rp1 = rendre
    return(rb20,rb10,rb5,rp2,rp1)
    

print(rendreMonnaie(222,(10,5,5,5,5)))
