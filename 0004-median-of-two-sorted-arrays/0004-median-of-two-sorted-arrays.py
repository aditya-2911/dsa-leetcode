class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)

        total=m+n
        i=j=0

        prev=curr=0

        for ct in range(total//2+1):
            prev=curr
            if i<m and j<n:
                if nums1[i]<=nums2[j]:
                    curr=nums1[i]
                    i+=1
                else:
                    curr=nums2[j]
                    j+=1
                
            elif i<m:
                curr=nums1[i]
                i+=1
            else:
                curr=nums2[j]
                j+=1
        
        if total&1:
            return curr
        else:
            return (prev+curr)/2
                