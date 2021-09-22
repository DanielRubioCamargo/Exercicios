def merge_the_tools(string, k):
    mylist = []
    m = 0
    for x in range(len(string)//k):
        mylist.append(string[m:m+k])
        m += k
    
    for x in mylist:
        print(''.join(list(dict.fromkeys(x))))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)