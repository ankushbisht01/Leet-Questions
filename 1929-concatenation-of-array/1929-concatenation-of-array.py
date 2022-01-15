class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = []
        for i in nums:
            a.append(i)
        for i in nums:
            a.append(i)
        return a