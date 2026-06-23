class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        size = len(nums)
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        min_diff = float('inf')


        for i in range(0, size - 2):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            minimum_sum = nums[i] + nums[i+1] + nums[i+2]
            if minimum_sum > target:
                if abs(minimum_sum - target) < min_diff:
                    result = minimum_sum
                break
                
            maximum_sum = nums[i] + nums[-1] + nums[-2]
            if maximum_sum < target:
                if abs(maximum_sum - target) < min_diff:
                    min_diff = abs(maximum_sum - target)
                    result = maximum_sum
                continue
            
            leftPtr, rightPtr = i + 1, size - 1
            while leftPtr < rightPtr:
                currentSum = nums[leftPtr] + nums[rightPtr] + nums[i]
                if currentSum == target:
                    return currentSum

                
                elif currentSum < target:
                    diff = abs(currentSum - target)
                    if diff < min_diff:
                        min_diff=diff
                        result= currentSum
                    leftPtr += 1
                else:
                    diff = abs(currentSum - target)
                    if diff < min_diff:
                        min_diff = diff
                        result = currentSum
                    rightPtr -= 1
        return result