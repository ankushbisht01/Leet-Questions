class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = []
        b = nums
        for i in nums:
            a.append(i)
        for j in b:
            a.append(j)
        return a