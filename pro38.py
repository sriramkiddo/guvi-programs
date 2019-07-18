n3,k3 = map(int,input().split())
S3 = list(map(int,input().split()))
count= 0
for i in S3:
    if(i+k <=5):
        count+=1
print(count//3)
