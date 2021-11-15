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
    sClassCopy = sClass[:]
    lowerGrade = sClassCopy[0][1]
    for c in sClassCopy:
        if c[1] < lowerGrade:
            lowerGrade = c[1]
    for i,c in enumerate(sClassCopy):
        if c[1] <= lowerGrade:
            sClassCopy.pop(i)
    for i,c in enumerate(sClassCopy):
        if c[1] <= lowerGrade:
            sClassCopy.pop(i)
    print(sClassCopy)
    if sClassCopy[0][1] != lowerGrade:
        lowerGrade = sClassCopy[0][1]
    for c in sClassCopy:
        if c[1] < lowerGrade:
            lowerGrade = c[1]
    sortedList = list()
    for i,c in enumerate(sClassCopy):
        if c[1] == lowerGrade:
            sortedList.append(c[0])
    sortedList.sort()
    for c in sortedList:
        print(c)
   

