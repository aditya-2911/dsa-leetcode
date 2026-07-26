class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for i,c in enumerate(words):
            if x in c:
                ans.append(i)
        return ans