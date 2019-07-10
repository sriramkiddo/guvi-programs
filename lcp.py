pt1=int(input())
ot1=[]
for hr in range(0,pt1):
 pant1=input()
 ot1.append(pant1)
de=[]
for hr in zip(*ot1):
 if(hr.count(hr[0])==len(hr)):
  de.append(hr[0])
 else:
  break
print(''.join(de))
