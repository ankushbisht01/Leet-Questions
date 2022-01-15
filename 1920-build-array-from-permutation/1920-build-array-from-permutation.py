class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0,len(nums)):
            result.append(nums[nums[i]])
        return result