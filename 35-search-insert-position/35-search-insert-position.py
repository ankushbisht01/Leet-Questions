class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums)-1
        
        while start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end = mid -1
            else:
                start = mid +1
        else:
            start = 0 
            end = len(nums)-1

            while start<=end:
                mid = (start+end)//2
                if nums[end]<target:
                    return end+1
                elif nums[start]>target:
                    return start  
                elif nums[mid]>target:
                    end = mid -1
                else:
                    start = mid +1
            return mid
            