class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            dig = nums.pop(0)
            sol = [i+x+1 for x in range(len(nums)) if (nums[x]+dig == target)]
            if sol != [] :
                return [i,sol[0]]
                break