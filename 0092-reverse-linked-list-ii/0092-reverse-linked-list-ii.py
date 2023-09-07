# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        a = prev =  head 
        count = 1 
        while(count < left):
            if count != 1:
                prev = prev.next 
            a = a.next 
            count+=1
        
        temp = a 
        b = a.next 
        while(b and count < right):
            a.next  = b.next 
            b.next = temp 
            temp = b
            b = a.next 
            count+=1
        if left == 1 :
            return temp
        prev.next = temp
        
        return head 
        