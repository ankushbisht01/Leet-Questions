class Solution {
public:
    int reverse(int x) {
        int sign = 1 ;
        if (x < 0 ){
            sign = -1 ;
            x = abs(x);
        }
        
        long result = 0 ;
        int max = INT_MAX ;
        while (x>0){
             
            result = x%10  + result*10;
            x/=10;
            if (  result > INT_MAX) return 0 ;
            else if (  result < -INT_MAX) return 0 ;
        }
        
        
        
        return sign*result;
    }
};