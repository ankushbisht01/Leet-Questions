"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        def postordertransversal(root):
            if root != None :
                for node in root.children:
                    postordertransversal(node)
                result.append(root.val)
        postordertransversal(root)
        return result