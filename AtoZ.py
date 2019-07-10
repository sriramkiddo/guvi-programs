k,l=map(str,input().split())
S=0
if len(k)>len(l):
    k,l=l,k
p=0
while p<len(k):
      S+=(ord(l[p])-ord(k[p]))
      p+=1
for p in range(p,len(k)):
      S+=ord(k[p])-ord('a')+1
print(S)
