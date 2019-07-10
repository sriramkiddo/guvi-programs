t,a=input().strip().split(" ")
a=int(a)
j=0;
while j<len(t)-1 and a:
    if(t[j]>t[j+1]):
        a-=1
        t=t[:j]+t[j+1:]
        if(j!=0):
            j-=1
    else:A
        j+=1
s=t[:len(t)-a]
print(s)
