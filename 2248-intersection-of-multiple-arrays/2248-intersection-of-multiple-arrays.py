class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1:
            nums[0].sort()
            return nums[0]
        old = set()
        for i in nums[0]:
            old.add(i)
            
        for i in range(1 , len(nums)):
            temp = set()
            for j in nums[i] :
                if j in old:
                    temp.add(j)
            old = temp 
        result =  list(old)
        result.sort()
        return result 
                    
        