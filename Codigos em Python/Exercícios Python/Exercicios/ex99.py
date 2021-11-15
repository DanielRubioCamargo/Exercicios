if __name__ == '__main__':
    data = list()
    sClass = list()
    n = int(input())
    for c in range(n):
        name = input()
        score = float(input())
        data.append(name)
        data.append(score)
        sClass.append(data[:])
        data.clear()
    lowerGrade = sClass[0][1]
    for c in sClass:
        if c[1] < lowerGrade:
            lowerGrade = c[1]
    for i,c in enumerate(sClass):
        if c[1] == lowerGrade:
            
   

