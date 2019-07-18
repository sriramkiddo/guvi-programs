p3,q3=input().split()
p3=int(p3)
q3=int(q3)
s3=''
u3=2
if(p3+q3<=3):
    for i in range(0,p3+q3):
        if(i%2!=0):
            s3=s3+'0'
        else:
            s3=s3+'1'
else:    
    for i in range(0,p3+q3):
        if(i==u3):
            s3=s3+'0'
            if(u3==q3):
                u3=u3+2
            else:
                u3=u3+3
        else:
            s3=s3+'1'
x=len(s3)-1
if(int(s3[x])==0):
    print('-1') 
elif p3==1 and q3==2: 
     print("011")
else:
    print(s3)
