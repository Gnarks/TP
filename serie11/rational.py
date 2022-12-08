import math

class Rational:
    def __init__(self,a=0,b=1) -> None:
        if type(a) == str:
            a = a.replace(" ","")
            for i in a:
                if i not in "/.1234567890":
                    raise ValueError(f"Cannot create a rational from this str: {a}")
            
            if len(a) == 3 and a[1] == "/":
                self.a = int(a[0])
                self.b = int(a[2])
                b = int(a[0])
                a = int(a[2])
            else:
                a = float(a)
        else:
            self.a = a
            self.b = b
            
        if type(a) == float:
            i = 0
            while (a%1 != 0 and i <7):
                a = round((a)*(10),7)
                i+=1
            self.a = int(a)
            self.b = 10**i
        elif type(a) != int:
            raise ValueError(f"Cannot create a rational with a numerator of {type(a)}")
        elif type(b) != int:
            raise ValueError(f"Cannot create a rational with a denominator of {type(b)}")
        elif b == 0:
            raise ZeroDivisionError(f"cannot create {a}/0 : zero in denominator")
        if self.a%self.b==0:
            self.a = self.a//self.b
            self.b = 1
        gcd = math.gcd(self.a,self.b)
        self.a = self.a// gcd
        self.b = self.b// gcd
        if self.b <0:
            self.a = self.a*-1
            self.b = self.b*-1
            
    def __str__(self) -> str:
        if self.b == 1:
            return str(self.a//self.b)
        return f"{self.a}/{self.b}"
    
    def __repr__(self) -> str:
        return f"Rationnal({self.a},{self.b})"
    
    def get_denominator(banane):
        return banane.b
    
    def get_numerator(bananebleue):
        return bananebleue.a
    
    def __add__(self,other):
        if type(other) != Rational:
            other = Rational(float(other))
        if self.b == other.b:
            return Rational(self.a+other.a,self.b)
        else:
            a = self.a*other.b+other.a*self.b
            b = self.b * other.b
            return Rational(a,b)
            
    def __radd__(self,other):
        return self.__add__(other)
        
    def __mul__(self,other):
        if type(other) != Rational:
            other = Rational(float(other))
        a = self.a*other.a
        b = self.b*other.b
        return Rational(a,b)
    
    def __rmul__(self,other):
        return self.__mul__(other)
    
    def __float__(self):
        return float(self.a/self.b)
    
    def __truediv__(self,other):
        if type(other) != Rational:
            other = Rational(float(other))
        return self.__mul__(Rational(other.b,other.a))
    
    def __sub__(self,other):
        if type(other) != Rational:
            other = Rational(float(other))
        return self.__add__(Rational(-other.a,other.b))

    def __rtruediv__(self,other):
        if type(other) != Rational:
            other = Rational(float(other))
        return other.__mul__(Rational(self.b,self.a))
    
    def __rsub__(self,other):
        return self.__sub__(other)
