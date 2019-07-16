ny=int(input())
lis1=list(map(int,input().split()))
bin1=[bin(x)[2:] for x in lis1]
bin1.sort(reverse=True)
for i in bin1:
    print(int(i,2))
