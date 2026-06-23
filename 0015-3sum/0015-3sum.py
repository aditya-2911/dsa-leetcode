class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        tripletArray = []
        size = len(nums)
        nums.sort()

        for i in range(0, size - 2):

            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            leftPtr, rightPtr = i + 1, size - 1
            while leftPtr < rightPtr:
                currentSum = nums[leftPtr] + nums[rightPtr]
                if currentSum == target:
                    tripletArray.append([nums[i], nums[leftPtr], nums[rightPtr]])
                    leftPtr += 1
                    rightPtr -= 1
                    while leftPtr < rightPtr and nums[leftPtr] == nums[leftPtr - 1]:
                        leftPtr += 1
                    while leftPtr < rightPtr and nums[rightPtr] == nums[rightPtr + 1]:
                        rightPtr -= 1

                elif currentSum < target:
                    leftPtr += 1
                else:
                    rightPtr -= 1
        return tripletArray
