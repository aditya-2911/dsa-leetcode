class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        b = len(needle)
        for i in range(len(haystack) - b + 1):
            j = 0
            while j < b and haystack[i + j] == needle[j]:
                j += 1

            if j == b:
                return i
        return -1
