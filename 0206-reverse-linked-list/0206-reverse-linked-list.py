# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not(head) :
            return head 
        a = temp = head 
        b = a.next 
        while(b):
            a.next = b.next 
            b.next = temp 
            temp = b 
            b = a.next 
        return temp
            
            
        