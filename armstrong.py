i=int(input())
j=len(str(i))
sum=0
temp=i
while temp>0:
    d=temp%10
    sum=sum+d**j
    temp//=10
if(i==sum):
    print("yes")
else:
    print('no')
