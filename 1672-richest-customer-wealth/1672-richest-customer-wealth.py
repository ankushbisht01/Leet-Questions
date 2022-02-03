class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = [] 
        for i in accounts:
            result.append(sum(i))
        return max(result)