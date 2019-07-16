n13=int(input())
li13=list(map(int,input().split()))
li13.sort()
a=0
b=0
for i in range(len(li13)):
    if li13[i]>=a:
        b=b+1
    a=a+li13[i]
print(b)
