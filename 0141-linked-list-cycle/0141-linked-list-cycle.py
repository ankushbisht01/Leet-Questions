# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if (head == None):
            return False
        slow = head
        fast = head.next 
        while(fast and fast.next):
            if (slow == fast ):
                return True
            slow = slow.next
            fast = fast.next.next 
        return False 
        