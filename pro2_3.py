m3,r3 = input().split()
m3,r3 = int(m3), int(r3)
Lt1 = [ int(x) for x in input().split()]
for i in range(0,r3) :
    at1,bt1 = input().split()
    at1,bt1 = int(at1), int(bt1)
for i in range(0,r3):
    print(min(Lt1[at1-1:bt1]))
