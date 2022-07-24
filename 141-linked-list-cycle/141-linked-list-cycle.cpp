/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == NULL||head->next==NULL) return false ;
        ListNode * fast = head ;
        ListNode * slow = head;
        
        while (fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
            if (slow==fast){
                return true;
            }
            
        }
        return false; 
    }
};