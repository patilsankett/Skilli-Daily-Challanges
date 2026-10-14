#Lowest Common Multiple (LCM) of Two Numbers
def findLcm(n1, n2):
    a,b = n1,n2
    while b!=0:
        a,b = b,a%b
    return n1 // a *n2