# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            if p is None and q is None:
                return True
            else:
                return False 
        a = self.isSameTree(p.left,q.left)
        if p.val!=q.val:
            return False
        b = self.isSameTree(p.right,q.right)
        if a == False or b == False:
            return False
        return True
        