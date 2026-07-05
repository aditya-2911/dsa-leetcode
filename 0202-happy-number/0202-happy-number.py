class Solution:
    def isHappy(self, n: int) -> bool:

        def digitSquare(num):
            return sum(int(char) ** 2 for char in str(num))

        slow = n
        fast = digitSquare(n)

        while fast != 1 and slow != fast:
            slow = digitSquare(slow)
            fast = digitSquare(fast)
            fast = digitSquare(fast)

        return fast == 1
