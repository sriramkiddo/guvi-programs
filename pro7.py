s=int(input())
m=0
for v in range(0,s):
  if(pow(2,v)>s):
    break
  m=s-pow(2,v)
print(m)
