x1 = int(input())
y1 = list(map(int, input().split()))
z3 = int(len(y1)/2)
if sum(y1[:z3])//len(y1[:z3]) == sum(y1[z3:])//len(y1[z3:]):
    print('yes')
else:
    print('no')
