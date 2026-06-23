class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positiveNums = []
        negativeNums = []
        squaredist=[]
        for num in range(len(nums)):
            if nums[num] < 0:
                negativeNums.insert(0, nums[num] ** 2)
            else:
                positiveNums.append(nums[num]**2)
        
        if len(positiveNums)==0:
            return negativeNums

        elif len(negativeNums)==0:
            return positiveNums
        
        else:
            positivePtr, negativePtr=0,0
            while positivePtr < len(positiveNums) and negativePtr < len(negativeNums):
                if positiveNums[positivePtr]<=negativeNums[negativePtr]:
                    squaredist.append(positiveNums[positivePtr])
                    positivePtr+=1
                else:
                    squaredist.append(negativeNums[negativePtr])
                    negativePtr+=1
                    
            if positivePtr < len(positiveNums):
                for i in range(positivePtr, len(positiveNums)):
                    squaredist.append(positiveNums[i])
                    
            elif negativePtr < len(negativeNums):
                for j in range(negativePtr, len(negativeNums)):
                    squaredist.append(negativeNums[j])
        
        
            return squaredist