# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode],values=None ) -> List[int]:
        if values==None:
            values=[]
        
        if root is None:
            return []
        self.inorderTraversal(root.left,values)
        values.append(root.val)
        self.inorderTraversal(root.right,values)
        
        return values
