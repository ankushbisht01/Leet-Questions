# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not(head):
            return head
        length = 0
        temp = head 
        temp1 = head
        while(temp.next ):
            length+=1 
            temp = temp.next
        length+=1
        step =  (k % length)
        if(step == 0): return head
        step = length - step
        for i in range(step-1):
            temp1 = temp1.next
        result = temp1.next
        temp.next = head 
        temp1.next = None
        return result
        