class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        size = len(nums)
        nums.sort()
        max_diff = float('inf')


        for i in range(0, size - 2):


            if i > 0 and nums[i] == nums[i - 1]:
                continue

            leftPtr, rightPtr = i + 1, size - 1
            while leftPtr < rightPtr:
                currentSum = nums[leftPtr] + nums[rightPtr] + nums[i]
                if currentSum == target:
                    return currentSum

                
                elif currentSum < target:
                    diff = abs(currentSum - target)
                    if diff < max_diff:
                        max_diff=diff
                        result= currentSum
                    leftPtr += 1
                else:
                    diff = abs(currentSum - target)
                    if diff < max_diff:
                        max_diff = diff
                        result = currentSum
                    rightPtr -= 1
        return result