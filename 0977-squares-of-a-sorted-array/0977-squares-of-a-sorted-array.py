class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positiveNums = []

        negativeNums = []
        squaredList = []
        for num in nums:
            if num < 0:
                negativeNums.append(num**2)
            else:
                positiveNums.append(num**2)
        negativeNums.reverse()
        if len(positiveNums) == 0:
            return negativeNums

        elif len(negativeNums) == 0:
            return positiveNums

        else:
            positivePtr, negativePtr = 0, 0
            while positivePtr < len(positiveNums) and negativePtr < len(negativeNums):
                if positiveNums[positivePtr] <= negativeNums[negativePtr]:
                    squaredList.append(positiveNums[positivePtr])
                    positivePtr += 1
                else:
                    squaredList.append(negativeNums[negativePtr])
                    negativePtr += 1

            if positivePtr < len(positiveNums):
                squaredList.extend(positiveNums[positivePtr:])

            elif negativePtr < len(negativeNums):
                squaredList.extend(negativeNums[negativePtr:])

            return squaredList
