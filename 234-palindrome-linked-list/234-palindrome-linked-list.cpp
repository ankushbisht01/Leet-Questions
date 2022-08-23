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
    bool isPalindrome(ListNode* head) {
        stack<int> mystack; 
        ListNode* copy = head ;
        int length = 0 ;
        while(copy!= NULL){
            length++;
            copy=copy->next;
        }
        
        int i =0 ;
        while(i < int(length/2) ){
            mystack.push(head->val);
            head = head->next;  
            i++;
        }
        if (length %2 != 0 ){
            head = head->next;
            i++;
        }
        int value ;
        while(i<length){
            value = head->val ;
            if ( value != mystack.top()){
                return false ;
            }
            head=head->next;
            mystack.pop();
            i++;
            
        }
        return true;
        
        
    }
};