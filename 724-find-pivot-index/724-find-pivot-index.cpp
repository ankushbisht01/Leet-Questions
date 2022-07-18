class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        vector<int>::iterator it;
        int sum=0 , cumilative = 0;
        for (it = nums.begin();it<nums.end();it++){
            sum=sum+*it;
        }
        int count=0;
        for (it = nums.begin();it<nums.end();it++){
            if (cumilative==(sum-cumilative-*it)){
                return count ;
            }
            cumilative = cumilative+ *it;
            count++;
        }
        return -1;
    }
};