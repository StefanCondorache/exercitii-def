def int_cit():                                                  #<
    n , list1 = int(input('numearul de elemente: ')) , []       #<    crearea unei
    for i in range(n):                                          #<    unei liste
        x=int(input('elementul integer '+str(i)+' ; '))         #<    cu elemente                                       
        list1.append(x)                                         #<    de tip
    return 'list_int:', list1                                   #<    integer
print(int_cit())                                                #<


def float_cit():
    n , list1 = int(input('numearul de elemente: ')) , []       #<    crearea unei
    for i in range(n):                                          #<    unei liste
        x=float(input('elementul integer '+str(i)+' ; '))       #<    cu elemente
        list1.append(x)                                         #<    de tip
    return 'list_float', list1                                  #<    float
print(float_cit())

def suma():                                                 #<      suma
    return 'S=',sum([0.5**j for j in range(9)][2::2])+1     #<      S=1+0.5**2+...
print(suma())                                               #<


import math
def combinari():                                                                    #<  
    n , m = int(input('n; ')) , int(input('m; '))                                   #<  combinatii
    if n>m:                                                                         #<  combinatii
        return 'C=', math.factorial(n)/(math.factorial(m)*(math.factorial(n-m)))    #<  combinatii
print(combinari())                                                                  #<


from fractions import Fraction                                                                          #<
def frac_ad():                                                                                          #<
    a1 , a2 , b1 , b2 =int(input('a1: ')),int(input('a2: ')),int(input('b1: ')),int(input('b2: '))      #<
    x=str(input('suma sau produs? :'))                                                                  #<      fractii
    if x=='s' or x=='suma':                                                                             #<      fractii
        return Fraction(a1,a2)+Fraction(b1,b2)                                                          #<      fractii
    elif x=='p' or x=='produs':                                                                         #<      fractii
        return Fraction(a1,a2)*Fraction(b1,b2)                                                          #<
    else:                                                                                               #<
        return 'nu am inteles ce doresti'                                                               #<
print(frac_ad())