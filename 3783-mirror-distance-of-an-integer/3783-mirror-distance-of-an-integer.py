class Solution:
    def mirrorDistance(self, n: int) -> int:
        ans=''
        num=n
        while n>0:
            ans+=str(n%10)
            n//=10
        print(ans)
        return abs(int(num)-int(ans))