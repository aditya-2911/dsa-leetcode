class Solution:
    def sumGame(self, num: str) -> bool:
        size=len(num)
        half=size//2

        lSum,rSum=0,0
        lQ,rQ=0,0

        for i in range(size):
            if num[i]=='?':
                if i<half:
                    lQ+=1
                else:
                    rQ+=1
            else:
                if i<half:
                    lSum+=int(num[i])
                else:
                    rSum+=int(num[i])
        
        if (lQ+rQ) & 1:
            return True
        
        if (lSum-rSum)==9*(rQ-lQ)//2:
            return False
        
        return True