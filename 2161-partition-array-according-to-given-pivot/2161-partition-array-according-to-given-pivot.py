class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, greater, equal = [], [], []

        for num in nums:
            if num == pivot:
                equal.append(num)
            elif num < pivot:
                less.append(num)
            else:
                greater.append(num)

        write_index = 0
        
        for num in less:
            nums[write_index] = num
            write_index += 1
            
        for num in equal:
            nums[write_index] = num
            write_index += 1
            
        for num in greater:
            nums[write_index] = num
            write_index += 1
        return nums
