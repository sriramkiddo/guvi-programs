num13=int(input())
mn13=input()
a=mn13.split(" ")
p=[]
for i in a:
    p.append(int(i))
q=[]

for j in range(0,num13):
    c = 1
    for k in range(j+1,num13):
        if p[j]<p[k]:
            c+=1
            p[j]=p[k]


        #print(j,k,c,p)
    q.append(c)

print(max(q))
