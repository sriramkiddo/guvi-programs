st13=input()
a13=0
for i in range(0,len(st13)):
    sv13=st13[0:i]+st13[i+1::]
    if(int(sv13)%8==0):
        a13=1
        break
if(a13==1):
    print("yes")
else:
    print("no")
