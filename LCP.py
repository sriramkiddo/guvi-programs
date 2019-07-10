pt1=int(input())
ot1=[]
for hr in range(0,pt1):
 pant1=input()
 ot1.append(pant1)
de=[]
for hr1 in zip(*ot1):
 if(hr1.count(hr1[0])==len(hr1)):
  de.append(hr[0])
 else:
  break
print(''.join(de))
