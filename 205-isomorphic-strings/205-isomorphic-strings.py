class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map <char , char> m1;
        map <char , char> m2;
        char first , second ;
        for (int i=0; i<s.length();i++){
            first = s[i];
            second = t[i];
            if (!m1[first]){
                m1[first]=second;
            }
            else if(m1[first]!=second){
                return false ;
            }
            if (!m2[second]){
                m2[second]=first;
            }
            else if(m2[second]!=first){
                return false ;
            }
            
        }
        return true ;
        
    }
};