n13,w13=map(int,input().split())
weights=list(map(int,input().split()))
val13=list(map(int,input().split()))
r=[]
for i in range(n13):
    if(weights[i]>w13):
        del weights[i]
        del val13[i]
n13=len(val)
for i in range(n13):
    r.append(val13[i]/weights[i])
sum=0
tot=0
l=sorted(zip(r,val13,weights),reverse=True)
for _,x,y in l:
    if(sum+y<=w13):
        sum+=y
        tot+=x
print(tot)
