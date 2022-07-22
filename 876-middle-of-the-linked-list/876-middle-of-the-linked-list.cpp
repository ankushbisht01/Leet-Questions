/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int len=0 ;
        ListNode* copy = head;
        while (copy != NULL){
            len++;
            copy = copy->next;
        }
        int middle = len/2;
        
        while (middle!=0){
            head = head->next;
            middle--;
        }
        return head;
    }
};