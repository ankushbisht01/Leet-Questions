class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
    vector<int> sum ;
    int cumilative_sum  = 0;
    vector<int> :: iterator it ;
    for (it= nums.begin();it<nums.end();it++){
        cumilative_sum += *it;
        sum.push_back(cumilative_sum);
    }
        return sum;
    }
};