num1=int(input())
lis3=[]
for i in range(num1):
    h=input()
    s=list(map(int,h.split()))
    lis3=lis3+s
lis3.sort()
for i in lis3:
    print(i,end=" ")
