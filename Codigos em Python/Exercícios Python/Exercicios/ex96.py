# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
s = str(input())
lst = s.split(" ")
auxLst = []
contLst = []
for c in lst:
    c = int(c)
for c in lst:
    if c not in auxLst:
        auxLst.append(c)
for c in auxLst:
    contLst.append(0)
for c in lst:
    for i,d in enumerate(auxLst):
        if c == d:
            contLst[i]+=1
for i,c in enumerate(contLst):
    if c == 1:
        print(auxLst[i])
        break
