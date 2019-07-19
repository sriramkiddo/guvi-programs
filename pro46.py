p3=int(input())
q3=list(map(int,input().split()))
a3=0
b3=0
q3.sort(reverse=True)
for i in q3:
  q3=a3+i
  if b3>q3:
    a3=q3
  else:
    a3=b3
    b3=q3
print(a3,b3)
