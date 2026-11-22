class Solution:
    def checkString(self, s: str) -> bool:
        flag=False

        for i in s:
            if i=='a' and flag:
                return False
            elif i=='b':
                flag=True
        return True