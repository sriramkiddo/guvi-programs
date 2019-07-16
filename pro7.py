sm=int(input())
ms=0
for v in range(0,sm):
  if(pow(2,v)>sm):
    break
  ms=sm-pow(2,v)
print(ms)
