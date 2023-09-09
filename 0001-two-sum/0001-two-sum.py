class Solution(object):
    def twoSum(self, nums, target):
        check = dict()
        result = []
        for i in range(len(nums)):
            diff = target- nums[i]
            if (diff ) in check.keys():
                result.append(i)
                result.append(check[diff])
                return result
            check[nums[i]] = i
        
            