class Solution {
public:
    bool isSubsequence(string s, string t) {
        for (char c:s){
            string s1 = t;
            for (int i = 0 ; i < t.length();i++){
                if (c==t[i]){
                    t=t.substr(i+1,t.length());
                    break;
                }
            }
            if (s1 == t){
                return false;
            }
        }
        return true;
    }
};