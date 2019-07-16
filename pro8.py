import math
sri,ram=map(int,input().split())
m1=[]
ktm=list(map(int,input().split()))
for j in range(0,ram):
    pt,qt=map(int,input().split())
    m1.append([pt,qt])
for j in m1:
    x=j[0]-1
    y=j[1]-1
    print(math.gcd(ktm[x],ktm[y]))
