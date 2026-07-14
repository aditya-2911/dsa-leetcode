class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit1,fruit2=-1,-1
        continousFruits=0
        currentNum=0
        maximum=0

        for f in fruits:
            if f==fruit1 or f==fruit2:
                currentNum+=1
            else:
                currentNum=continousFruits+1

            if f==fruit2:
                continousFruits+=1
            else:
                continousFruits=1
                fruit1,fruit2=fruit2,f

            maximum=max(maximum,currentNum)

        return maximum