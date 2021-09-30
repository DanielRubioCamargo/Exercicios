if __name__ == '__main__':
    s = input()
    cont = 0
    for i in s:
        if i.isalpha() == True or i.isnumeric == True:
            cont+=1
    if cont > 0:
        print(True)
    else:
        print(False)
    cont = 0
    for i in s:
        if i.isalpha() == True:
            cont+=1
    if cont > 0:
        print(True)
    else:
        print(False)
    cont = 0
    for i in s:
        if i.isnumeric() == True:
            cont+=1
    if cont > 0:
        print(True)
    else:
        print(False)
    cont = 0
    for i in s:
        if i.islower() == True:
            cont+=1
    if cont > 0:
        print(True)
    else:
        print(False)   
    cont = 0
    for i in s:
        if i.isupper() == True:
            cont+=1
    if cont > 0:
        print(True)
    else:
        print(False)    
        
        