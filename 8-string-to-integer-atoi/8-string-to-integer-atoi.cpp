class Solution {
public:
    int myAtoi(string s) {
        if (s.length() == 0 ) return 0;
        
        int i=0;
        while (s[i]==' '){
            i++;
        }
        s = s.substr(i);
        int sign = 1 ;
        if (s[0]=='-') {
            sign = -1 ;
            s = s.substr(1);
        }
        else if (s[0]=='+')
        {
            s = s.substr(1);
        }
        int max = INT_MAX ;
        long  result = 0 ;
        for (int i =0 ; i < s.length() && isdigit(s[i]);i++){
            result = result * 10 + int(s[i]) - 48;
            if (  result > INT_MAX and sign==-1) return sign*max -1 ;
            else if (  result > INT_MAX) return sign*max ;
        }
        
        
        
        
        return sign * result ;
    }
};