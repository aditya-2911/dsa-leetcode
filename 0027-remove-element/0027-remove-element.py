class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j=-1,len(nums)-1

        while i<j:
            if nums[i+1]!=val:
                i+=1
            else:
                nums[i+1],nums[j]=nums[j],nums[i+1]
                j-=1
        return i+1