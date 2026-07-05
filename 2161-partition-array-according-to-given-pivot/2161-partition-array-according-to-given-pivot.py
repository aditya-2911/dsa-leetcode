class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        size = len(nums)
        res = [0]*size

        leftW = 0
        rightW = size - 1

        l, r = 0, size - 1

        while l < size:
            if nums[l] < pivot:
                res[leftW] = nums[l]
                leftW += 1
            if nums[r] > pivot:
                res[rightW] = nums[r]
                rightW -= 1

            l += 1
            r -= 1

        while leftW<=rightW:
            res[leftW]=pivot
            leftW+=1
        
        return res
