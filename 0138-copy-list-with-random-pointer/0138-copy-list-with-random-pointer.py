"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        start = head 
        start1 = head 
        result = Node(0)
        temp = result
        
        addr = {}
        while(start):
            newNode = Node(start.val )
            addr[start] = newNode 
            start = start.next 
            result.next = newNode
            result = result.next
            
        temp1 = temp.next 
        while(start1):
            if start1.random == None:
                temp1
                pass
            else:
                temp1.random = addr[start1.random]
            temp1 = temp1.next 
            start1 = start1.next
        return temp.next
        
        
        
        
        
            
            
        
        