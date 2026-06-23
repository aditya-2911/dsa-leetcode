class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(low, high):
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[high] = nums[high], nums[i + 1]
            return i + 1
        
        def sort(low, high):
            if low < high:
                pi = partition(low, high)
                sort(low, pi - 1)
                sort(pi + 1, high)
        
        sort(0, len(nums) - 1)
