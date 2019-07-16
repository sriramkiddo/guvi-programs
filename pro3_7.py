A13,B13=map(int,input().split())
C13=list(map(int,input().split()))
pr=list(map(int,input().split()))
qr=[]
ar=0
for i in range(A13):
    x=pr[i]/C13[i]
    qr.append(x)
while B13>=0 and len(qr)>0:
    mindex=qr.index(max(qr))
    if B13>=C13[mindex]:
        ar=ar+pr[mindex]
        B13=B13-C13[mindex]
    C13.pop(mindex)
    pr.pop(mindex)
    qr.pop(mindex)
print(ar)
