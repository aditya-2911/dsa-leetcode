class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        fptr=0

        for sptr in range(1,len(nums)):
            if nums[sptr] != nums[fptr]:
                fptr=fptr+1
                nums[fptr]=nums[sptr]
                k+=1
            else:
                sptr=sptr+1
        return k