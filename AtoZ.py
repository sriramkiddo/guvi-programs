k,l=map(str,input().split())
yas=0
if len(k)>len(l):
  k,l=l,k
p=0
while p<len(k):
  yas+=(ord(l[p])-ord(k[p]))
  p+=1
for p in range(p,len(l)):
  yas+=ord(l[p])-ord('a')+1
print(yas)
