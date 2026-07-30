class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low,high=0,len(nums)-1
        ans=[]
        while low<=high:
            mid=low+(high-low)//2

            if nums[mid]==target:
                if mid==0 or nums[mid-1]<target:
                    ans.append(mid)
                    break
                else:
                    high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        if not ans:
            return [-1,-1]

        low,high=0,len(nums)-1

        while low<=high:
            mid=low+(high-low)//2

            if nums[mid]==target:
                if mid ==len(nums)-1 or nums[mid+1]>target:
                    ans.append(mid)
                    break
                else:
                    low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        
        return ans if ans else [-1,-1]
        


