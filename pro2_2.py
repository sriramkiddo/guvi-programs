m3,r3=list(map(int,input().split()))
lis3=list(map(int,input().split()))
for i in range(r3):
  ut3,vt3=list(map(int,input().split()))
  print(sum(lis3[ut3-1:vt3]))
