n1 = int(input())
s = 0
for i in range(2,n1):
    if(n1%i == 0):
        c+=1
if(s == 0):
    print("yes")
else:
    print("no")
