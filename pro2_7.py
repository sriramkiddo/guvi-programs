al=input()

a=list(map(int,al.split()))

k1=a[1]
h1=input()

s=list(map(int,h1.split()))
flag=0
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]+s[j]==k1:
            print("yes")
            flag=1
            break
    if flag==1:
        break
if flag!=1:
    print("no")
