class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0 
        for i in digits :
            result = result*10 + i
        result+=1
        digits = []
        while result >0 :
            remainder = result %10
            digits.append(remainder)
            result = result //10
        return digits[::-1]
                