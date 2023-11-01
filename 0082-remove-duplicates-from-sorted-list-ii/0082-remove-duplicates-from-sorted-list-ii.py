# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = None 
        curr = temp = head
        fast = head.next
        while(fast != None):
            if (curr.val == fast.val):
                while(fast.next and fast.val == fast.next.val):
                    fast = fast.next
                if(prev == None):
                    temp = fast.next
                else:
                    prev.next = fast.next
                curr = fast.next
                if (curr != None):
                        fast = curr.next
                else:
                    break
            else:
                        prev = curr
                        curr = curr.next
                        fast = fast.next
        return temp
        
        