class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        size=len(tasks)
        res=[]
        
        prefix=[0]*(size+1)
        for i in range(size):
            prefix[i+1]=prefix[i]+tasks[i]

        def bs(target):
            l,r=0,size
            ans=0

            while l<=r:
                mid=l+(r-l)//2

                if prefix[mid]<=target:
                    ans=mid
                    l=mid+1
                else:
                    r=mid-1
            return ans

        req_time=prefix[-1]
        curr=0
        for i in shifts:
            curr+=i

            if curr>=req_time:
                res.append(0)
                curr=0
            else:
                completed=bs(curr)
                remaining=size-completed
                
                res.append(remaining)

        return res