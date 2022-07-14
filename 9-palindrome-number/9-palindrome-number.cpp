class Solution {
public:
    bool isPalindrome(int x) {
        unsigned int newnum = 0;
        int copy = x ;
        
            
        while(x>0){
            
            newnum = newnum*10 + (x%10) ;
            x = x/10;
            
        }
        if (newnum==copy){
            return true ;
        }
        return false;
        
    }
};