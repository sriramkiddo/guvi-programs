n3=int(input())
lis3=list(map(int,input().split()))
choco=1
count=0
if lis3[0]>lis3[1]:
    choco=choco+1
    count=count+choco
else:
    count=choco
for i in range(1,len(lis3)):
    if lis3[i]>lis3[i-1]:
        choco=choco+1
        count=count+choco
    else:
        choco=1
        count=count+choco
print(count)
