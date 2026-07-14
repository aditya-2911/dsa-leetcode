class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        size=len(nums2)
        seen={}
        stack=[]

        for i in range(size-1,-1,-1):
            while stack and nums2[i]>=stack[-1]:
                stack.pop()
                
            if not stack:
                seen[nums2[i]]=-1
            else:
                seen[nums2[i]]=stack[-1]
            stack.append(nums2[i])


        return [seen[x] for x in nums1]
