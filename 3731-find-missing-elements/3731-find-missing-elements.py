class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxVal,minVal=max(nums),min(nums)

        nums=set(nums)

        ans=[]

        for i in range(minVal+1,maxVal):
            if i not in nums:
                ans.append(i)
        return ans