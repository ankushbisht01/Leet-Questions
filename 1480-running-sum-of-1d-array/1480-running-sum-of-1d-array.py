class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        result = []
        for x in nums:
            sum=sum+x
            result.append(sum)
        return result