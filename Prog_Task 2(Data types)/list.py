if __name__ == '__main__':
    N = int(input())
    ls = []
    for i in range(N):
        m = list(input().split())
        if m[0]=='insert':
            ls.insert(int(m[1]),int(m[2]))
        if m[0]=='remove':
            ls.remove(int(m[1]))
        if m[0]=='append':
            ls.append(int(m[1]))
        if m[0]=='sort':
            ls.sort()
        if m[0]=='pop':
            ls.pop()
        if m[0]=='reverse':
            ls.reverse()     
        if m[0]=='print':
            print(ls)
