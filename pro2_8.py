ar,br=map(int,input().split())
l=[]
for _ in range(ar):
    l.append(input())
for i in range(len(l)):
    if('0' in l[i]):
        l[i]=l[i].replace('0','')
    l[i]=l[i].replace(' ','')
lengths=[]
for i in l:
    if(len(i)>0):
        lengths.append(len(i))
br=min(lengths)
r='1 '*br
r=r.strip()
for i in range(br):
    print(r)
