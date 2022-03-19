# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
    
        length = 0 
        length_tem = head
        while length_tem is not None:
            length +=1 
            length_tem = length_tem.next

        curr = head 
        for i in range(length-n-1):
            curr = curr.next
        if length - n == 0 :
            head = curr.next
        if curr.next is  None:
            curr.next = None
        else:
            curr.next = curr.next.next
        return head