# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if (root == None):
            return []
        
        l1 = self.inorderTraversal(root.left)
        l1.append(root.val)
        l2 = self.inorderTraversal(root.right)
       
        return l1 + l2
        