class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        size=len(arr)
        stack=[]
        max_area=0

        for i in range(size+1):
            if i==size:
                curr_height=0
            else:
                curr_height=arr[i]
            
            while stack and curr_height<arr[stack[-1]]:
                height=arr[stack.pop()]

                if not stack:
                    width=i
                else:
                    width=i-stack[-1]-1

                max_area=max(max_area, height*width)
            
            stack.append(i)
        return max_area