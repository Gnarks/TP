def puissance(x,n):
    if n < 0:
        return 1/puissance(x, -n)
    if n== 0:
        return 1
    if n==1:
        return x
    return x*puissance(x, n-1)

def contient(n,d):
    if str(n) in str(d):
        return True
    return False

def est_multiple(n,d):
    if d==0:
        return True
    elif d<0:
        return False
    return est_multiple(n,d-n)

def ackermann(m,n):
    return n+1 if m==0 else ackermann(m-1,1) if m>0 and n==0 else ackermann(m-1,ackermann(m,n-1)) if m>0 and n> 0 else None

def triangle_pascal(n,p):
    if n == 0 and p == 0:
        return 1
    elif n<0 or p<0:
        return 0
    return triangle_pascal(n-1,p-1) + triangle_pascal(n-1,p)
    
    