

# Complete the solve function below.
def solve(s):
    stringList = s.split(" ")
    lastList = list()
    for c in stringList:
        lastList.append(c.capitalize())
    return " ".join(lastList)

if __name__ == '__main__':

    s = input()

    result = solve(s)
    print(result)

    