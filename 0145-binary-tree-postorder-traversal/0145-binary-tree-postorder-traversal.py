# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorder(self , root , result):
        if root == None:
            return result
        else:
            self.postorder(root.left , result)
            self.postorder(root.right , result)
            result.append(root.val)
            return result 
            
    def postorderTraversal(self, root):
        result = self.postorder(root , [])
        return result 
        