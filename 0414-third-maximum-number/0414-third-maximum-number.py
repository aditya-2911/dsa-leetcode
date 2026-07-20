class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1=max2=max3=float('-inf')


        for i in nums:
            if i==max1 or i==max2 or i==max3:
                continue
            if i>max1:
                max3=max2
                max2=max1
                max1=i
            elif i>max2 and i<max1:
                max3=max2
                max2=i
            elif i>max3 and i<max2:
                max3=i
        return max3 if max3!=float('-inf') else max1