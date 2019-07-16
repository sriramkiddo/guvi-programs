get1=int(input())
set1=list(map(int,input().split()))
go=0
for one1 in range(get1):
    for two2 in range(one1,get1):  
        for three3 in range(two2,get1):
            if set1[one1]<set1[two2]<set1[three3]:
                go+=1
print(go)
