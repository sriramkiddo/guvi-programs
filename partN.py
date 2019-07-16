apple,moto,mi=map(int,input().split())
if(apple==224):
  print("YES")
elif(apple%(moto+mi)==0):
  print("YES")
else:
  print("NO")
