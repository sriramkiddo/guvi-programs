n13=int(input())
a=0
b=0
li13=[]
while(a<90 and a<n13):
  s=0
  for j in str(n13-a):
    s+=int(j)
  if s+(n13-a)==n13:
    b+=1
    li13.append(n13-a)
  a+=1
print(b)
for i in li13:
  print(i)
