m3=int(input())
c3=0
l3=[]
for i in range(1,m3+1):
  l3.append(i)
for i in range(len(l3)):
  for i in range(i+1,len(l3)):
    c3+=1
print(c3)
