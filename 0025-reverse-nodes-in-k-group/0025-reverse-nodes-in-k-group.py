# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head == None or  k == 1):
            return head
        prev = curr = head 
        fast = head.next 
        end = None
        temp = 1 
        start = head 
        i = 1
        while(fast):
            
            curr.next = fast.next 
            fast.next = prev 
            prev = fast 
            fast = curr.next 
            temp +=1 
            if i == k-1 :
                start = prev
            i+=1
            if (temp == k ):
                temp = 1
                if (end):
                    end.next = prev
                end = curr
                prev = curr = fast 
                if (curr):
                    fast = curr.next
                else:
                    break
        if temp !=1:
            curr = prev
            if (curr):
                fast = curr.next 
            while(fast):
                curr.next = fast.next 
                fast.next = prev 
                prev = fast 
                fast = curr.next
            end.next = prev
            
        return start
                