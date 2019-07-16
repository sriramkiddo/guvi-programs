n3,money3=list(map(int,input().split()))
lis3=list(map(int,input().split()))
lis3.sort(reverse=True)
count3=0
for i in lis3:
    if money3==0:
        break
    q=money3//i
    count3=count3+q
    money3=money3-i*(q)
print(count3)
