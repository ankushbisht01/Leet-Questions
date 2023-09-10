class Solution(object):
    def isPalindrome(self, x):
        result = 0 
        temp = x
        rem = 0 
        while(temp > 0 ):
            rem = temp % 10 
            result = result * 10 + rem
            temp = temp //10
        return result == x
        