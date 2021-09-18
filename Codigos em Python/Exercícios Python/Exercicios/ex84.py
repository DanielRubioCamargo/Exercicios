def fatorial(n=1,show=False):
    fat = 1
    num = n
    for i in range(n,0,-1):
        fat*=n
        n-=1
    if show == True:
        for i in range(num,0,-1):
            if i != 1:
                print("{} X".format(i),end = " ")
            else:
                print("{} =".format(i),end = " ")
    print(fat)


fatorial(5,show=True)