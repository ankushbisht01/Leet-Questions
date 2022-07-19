// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long int min = 0 ;
        long int max = n;
        long int mid;
        bool check0 , check1 , check2;
        
        while(min<=max){
            mid = (min+max)/2;
            check0 = isBadVersion(mid);
            check1 = isBadVersion(mid-1);
            check2 = isBadVersion(mid+1);
            if (check0==true && check1 == true ){
                max=mid-2;
            }
            else if(check0==true && check1== false){
                return mid;
            }
            else if(check0==false && check2==true){
                return mid+1;
            }
            else if(check0==false && check2==false){
                min=mid+2;
            }
            
        }
        return 1;
    }
};