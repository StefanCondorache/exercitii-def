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