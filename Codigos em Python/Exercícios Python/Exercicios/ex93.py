if __name__ == '__main__':
    n = int(input())
    scores = list()
    highest = 0
    for i in range(n):
        score = int(input())
        scores.append(score)
        if score > highest:
            highest = score
    for i,c in enumerate(scores):
        if c == highest:
            scores.pop(i)
    highest2 = 0
    for i in scores:
        if i > highest2 and i != highest:
            highest2 = i
    print(highest2)
    print(scores)
    