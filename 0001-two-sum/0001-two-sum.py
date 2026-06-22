class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        num_dict = {}

        for i in range(len(numbers)):
            number=numbers[i]
            second_num= target-number
            
            if second_num in num_dict:
                return([num_dict[second_num], i])
            
            num_dict[number]=i
