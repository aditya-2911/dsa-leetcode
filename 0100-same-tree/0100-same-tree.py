# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        t1=[]
        t2=[]

        def post(node,ans):
            if node is None:
                ans.append(None)
                return
            
            post(node.left,ans)
            post(node.right,ans)
            ans.append(node.val)
        
        post(p,t1)
        post(q,t2)
        return t1==t2