class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n,len(nums)):
            result.append(nums[i-n])
            result.append(nums[i])
        return result