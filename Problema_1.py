def int_cit():                                                  #<
    n , list1 = int(input('numearul de elemente: ')) , []       #<    crearea unei
    for i in range(n):                                          #<    unei liste
        x=int(input('elementul integer '+str(i)+' ; '))         #<    cu elemente                                       
        list1.append(x)                                         #<    de tip
    return 'list_int:', list1                                   #<    integer
print(int_cit())                                                #<