br=input()
for i in range(1,len(br)):
    if ord(br[i])>ord(br[0]):
        ans=br[i:]
        break
print(ans)
