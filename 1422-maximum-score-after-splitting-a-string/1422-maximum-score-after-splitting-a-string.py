class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0 
        zero = 0 
        max = -1
        for i in s:
            if i == '1':
                ones+=1
        for i in range(len(s)-1):
            char = s[i]
            
            if char == '0':
                zero+=1
                sum = zero+ones
            else:
                ones-=1
                sum = zero +ones
            if sum > max :
                max = sum
        return max