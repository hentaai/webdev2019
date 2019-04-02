if __name__ == '__main__':
    n=int(input())
    s=set()
    for i in range(0,n):
        c=input()
        s.add(c)
    print(len(s))