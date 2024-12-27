import math

def kubus(s):
    luas=6*s*s
    print('luas permukaan kubus adalah', luas)
    
def balok(p,l,t):
    luas=2*(p*l+p*t+l*t)
    print('luas permukaan balok adalah', luas)
    
def tabung(r,t):
    luas=2*math.pi*r*(r+t)
    print('luas permukaan tabung adalah', luas)
    
def bola(r):
    luas=4*math.pi*r*r
    print('luas permukaan bola adalah', luas)
    
def kerucut(r,s):
    luas = 3.14 * r * ( r + s )
    print('luas  permukaan kerucut adalah', luas)