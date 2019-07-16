a1=int(input())
arr1=list(map(int,input().split()))
arr1.sort(reverse=True)
s=0
s1=0
res1=[]
for i in range(0,a1,2):
    s=s+arr1[i]
for j in range(1,a1,2):
    s1=s1+arr1[j]
res1.append([s,s1])
for i in res1:
    print(i[0] if i[0]>i[1] else i[1])
