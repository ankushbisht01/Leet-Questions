class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        vector<int> :: iterator it  ;
        string result(s.length(),'a');
        int i = 0 ;
        for (it=indices.begin();it!=indices.end();it++){
            result[*it]=  s[i];
            i++;
        }
        return result;
    }
};