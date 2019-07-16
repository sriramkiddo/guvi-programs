a1=int(input())
b1=list(map(int,input().split()))
m=0
for i in range(0,a1):
  for j in range(0,i):
    if(b1[j]<b1[i]):
      m=m+b1[j]
print(m)
