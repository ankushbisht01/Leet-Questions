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
    ListNode *detectCycle(ListNode *head) {
        if (head == NULL) return NULL;
        if (head->next == NULL) return NULL;
        map <ListNode* , int > addressmap;
        ListNode* copy = head;
        while(copy->next != NULL){
            if (!(addressmap[copy])){
                addressmap[copy]=1;
                copy= copy->next;
            }
            else{
                return copy;
            }
        }
        return NULL;
    }
};