class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums)-1
        count = 0
        low = 0 
        if len(nums)==1:
            if nums[0]==val:
                return 0
            else:
                return 1
        while (low<=end):
            if(nums[end] == val):
                end-=1
                count+=1
                
                continue
            if nums[low]==val:
                nums[low]=nums[end]
                end-=1
                count+=1
            low+=1
        
        return len(nums)-count