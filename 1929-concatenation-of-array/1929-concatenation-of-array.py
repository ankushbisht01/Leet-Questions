class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
     
        for j in range(len(nums)):
            nums.append(nums[j])
        return nums