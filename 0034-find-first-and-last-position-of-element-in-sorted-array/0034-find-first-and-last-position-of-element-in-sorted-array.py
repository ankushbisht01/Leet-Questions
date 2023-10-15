class Solution(object):
    def searchRange(self, nums, target):
        if (len(nums) == 0 ):
            return [-1,-1]
        if(len(nums) == 1 and nums[0] == target):
            return [0,0]
        low = 0 
        high = len(nums)-1
        mid = 0 
        i = 0 
        j = 0 
        
        while(low <= high):
            mid = (low+high)/2
            
            if (nums[mid] < target):
                low = mid + 1
            elif (nums[mid] > target):
                high= mid -1
            else:
                i = mid 
                j = mid
                while(i >0 and nums[i] == nums[i-1]):
                    i -=1
                while(j <(len(nums)-1) and nums[j] == nums[j+1]):
                    j+=1
                return [i,j]
        return [-1,-1]
                
        