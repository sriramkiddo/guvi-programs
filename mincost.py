r,a=input().split()
h1=abs(len(r)-len(a))
for i in range(len(r)):
  if len(a)==1 and a[i] in r:
    break
  if r[i]!=a[i]:
    h1=h1+1
print(h1)
