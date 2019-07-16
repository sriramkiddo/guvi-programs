pi,qi=map(int,input().split())
l=list(map(int,input().split()))
for i in range(qi):
    r,s=map(int,input().split())
    t1 = l[r-1:s]
    u1 = t1[0]
    for i in range(1,len(t1)):
        u1 = u1 ^ t1[i]
    print(u1)
