class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        maxGreen=max(lights)
        penalty=0

        for car in arrivalTime:
            r=car%period

            if r>=maxGreen:
                wait=period-r

                if wait>penalty:
                    penalty=wait
                

        return penalty