class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashcount = set(nums)
        return not(len(nums)==len(hashcount))