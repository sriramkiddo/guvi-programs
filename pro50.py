n3,m3=map(int,input().split())
e3=[]
for i in range(m3):
  e3.append(list(map(int,input().split())))
cost=10000000
f3=0
for i in range(m3):
  if e3[i][0]==1:
    s3=e3[i][1]
    c3=e3[i][2]
    for j in range(i+1,m3):
      if e3[j][0]==s3:
        s3=e3[j][1]
        c3+=e3[j][2]
    if c3<cost and s3==n3:
      cost=c3
      f3+=1
if f3==0:
  print(-1)
else:
  print(cost)
