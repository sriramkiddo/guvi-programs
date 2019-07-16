p,a=input().split()
h1=abs(len(p)-len(a))
for i in range(len(p)):
  if len(a)==1 and a[i] in p:
    break
  if p[i]!=a[i]:
    h1=h1+1
print(h1)
