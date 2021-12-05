if __name__ == '__main__':
    N = int(input())
    lst = list()
    for i in range(N):
        [op] = input().split(" ")
        op = str(op)
        n1 = 0
        n2 = 0
        if op == "insert":
            [n1,n2] = input().split()
            n1 = int(n1)
            n2 = int(n2)
            lst.insert(n2,n1)
        elif op == "append":
            [n1] = input().split()
            n1 = int(n1)
            lst.append(n1)
        elif op == "remove":
            [n1] = input().split()
            n1 = int(n1)
            lst.remove(n1)
        elif op == "pop":
            lst.pop()
        elif op == "reverse":
            lst.sort(reversed)
        elif op == "sort":
            lst.sort()
        elif op == "print":
            print(lst)