n12=int(input())
m12=input()
o=m12.split(" ")
p=[]
for i in o:
    p.append(int(i))
q=[]
count=1
for j in range(0,n12-1):
    if p[j]<p[j+1]:
        count+=1
    else:
        q.append(count)
        
        count=1
    
q.append(count)
print(max(q))
