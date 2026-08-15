class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        curr=0
        total=0

        for r in requests:
            total+=abs(curr-r)
            curr=r

        return total