class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
         result = [ (nums[nums[i]]) for i in range(0,len(nums))]
         return result