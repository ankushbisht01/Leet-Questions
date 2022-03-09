class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0 
        output=[]
        for i in digits:
            result = result*10+i
        result = result+ 1
        
        while (result>0):
            remainder = result%10
            output.append(remainder)
            result = result//10
        return output[::-1]