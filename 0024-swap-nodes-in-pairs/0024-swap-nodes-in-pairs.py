# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if (not(head) or not(head.next)):
            return head
        temp = head
        while(temp):
            if (not(temp.next)):
                break
            tempVal = temp.val
            temp.val = temp.next.val
            temp.next.val = tempVal
            temp = temp.next.next
            
        return head
        