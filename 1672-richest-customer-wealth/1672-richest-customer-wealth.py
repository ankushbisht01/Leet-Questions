class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = [] 
       
        for i in accounts:
            sum1 = 0 
            for j in i :
                sum1 += j
            result.append(sum1)
        max_elem = result[0]
        for i in result:
            if i > max_elem :
                max_elem = i 
        return max_elem