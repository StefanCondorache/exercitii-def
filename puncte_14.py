n1=int(input('n1: '))
n2=int(input('n2: '))

def suma(x,y):
    return x+y

def produs(x,y):
    return x*y

def media_aritmetica(x,y):
    return (x+y)/2

def divizor(x,y):
    return max([i for i in range(1,x+1) if x%i==0 and y%i==0])

def multiplu(x,y):
    for i in range(1,x**3):
        for j in range(1,y**3):
            if x*i==y*j:
                return '0 este multiplu pentru orice numar,'\
                    ' cel mai mic multiplu nenul:',x*i

def minim(x,y):
    return min([x,y])

def maxim(x,y):
    return max([x,y])

def suma_nr_citite():
    a=int(input('a: '))
    b=int(input('b: '))
    return 'c=',a+b

def produsul_nr_citite():
    a=int(input('a: '))
    b=int(input('b: '))
    return 'c=',a*b

def divizori_comuni(x,y):
    return [i for i in range(1,x+1) if x%i==0 and y%i==0]

def multipli_comuni(x,y):
    list1=[]
    for i in range(1,x**5):
        for j in range(1,y**5):
            if x*i==y*j:
                list1.append(x*i)
            if len(list1)==5:
                return list1

def cifre_comune(x,y):
    list1=[]
    for i in [j for j in str(x)]:
        for k in [l for l in str(y)]:
            if i==k:
                list1.append(int(i))
    return list1

def cifre_din_primul(x,y):
    list1=[]
    for i in [j for j in str(x)]:
        if i not in [l for l in str(y)]:
            list1.append(int(i))
    return list1

def prietenie(x,y):
    if len([i for i in range(1,x+1) if x%i==0])==len([i for i in range(1,y+1) if y%i==0]):
        return 'PRIETENIE'
    
