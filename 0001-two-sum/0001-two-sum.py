class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            n=target-numbers[i]
            for j in range(len(numbers)):
                if numbers[j]==n and i!=j:
                    return([i,j])
