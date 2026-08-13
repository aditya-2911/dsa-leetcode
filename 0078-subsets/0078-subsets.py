class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]

        def func(nums,n,i,temp):
            if i==n:
                res.append(temp[:])
                return
            
            func(nums,n,i+1,temp)
            temp.append(nums[i])
            func(nums,n,i+1,temp)
            temp.pop()

            return
        temp=[]
        i=0
        func(nums,n,i,temp)
        return res