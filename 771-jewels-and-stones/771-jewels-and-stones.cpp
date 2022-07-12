class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        if (jewels.length() == 0){ return 0; } 
        if (stones.length() == 0){ return 0;}
        int count=0;
        for (int i =0 ;i<jewels.length();i++){
            for (int j =0 ; j<stones.length();j++){
                if (jewels[i]==stones[j]){
                    count++;
                }
            }
            
        }
        return count;
        
    }
};