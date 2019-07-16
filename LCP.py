p=int(input())
o=[]
for hr1 in range(0,p):
 pan=input()
 o.append(pan)
de=[]
for hr1 in zip(*o):
 if(hr1.count(hr1[0])==len(hr1)):
  de.append(hr1[0])
 else:
  break
print(''.join(de))
