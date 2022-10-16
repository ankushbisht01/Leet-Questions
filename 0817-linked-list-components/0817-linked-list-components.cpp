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
    int numComponents(ListNode* head, vector<int>& nums) {
        unordered_set<int> hashset;
        
        for (int i = 0 ; i<nums.size(); i++){
            hashset.insert(nums[i]);
        }
        
        int noOfNodes = 0 ;
        ListNode * prev = NULL;
        ListNode * current = head;
        
        while(current !=NULL){
            if (prev == NULL ){
                if ( hashset.find(current->val) != hashset.end())
                noOfNodes++;
            }
            else if( hashset.find(prev->val)== hashset.end() && hashset.find(current->val)!= hashset.end() ){
                noOfNodes++;
            }
            
            prev = current;
            current = current->next;
        }
        
        return  noOfNodes;
    }
};