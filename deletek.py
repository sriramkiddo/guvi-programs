p,k=input().strip().split(" ")
k=int(k)
j=0;
while j<len(p)-1 and k:
    if(p[j]>p[j+1]):
        k-=1
        p=p[:j]+p[j+1:]
        if(j!=0):
            j-=1
    else:
        j+=1
s=p[:len(p)-k]
print(s)
