p3=int(input())
while p3%10==0:
  p3=p3//10
p3=str(p3)
re=p3[::-1]
if p3==re:
  print("yes")
else:
    print("no")
