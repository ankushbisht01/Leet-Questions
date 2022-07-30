class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if ( nums.size()<=1) return ;
        int size = nums.size();
        if (k > size ) k = k%size;
        int nonroot = size - k;
        int temp;
        for (int i = 0 ; i < (nonroot)/2 ; i++)
        {
            temp = nums[i];
            nums[i] = nums[nonroot-1-i];
            nums[nonroot-1-i]=temp;
        }
        int i = nonroot , j = size-1 ;
        while ( i<j){
            temp = nums[i];
            nums[i] = nums[j];
            nums[j]=temp;
            i++;
            j--;
        }
        for (int i = 0 ; i < (size)/2 ; i++){
            temp = nums[i];
            nums[i]= nums[size-1-i];
            nums[size-1-i]=temp;
        } 
        
        
    }
};