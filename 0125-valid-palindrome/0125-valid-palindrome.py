class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        result = ""
        for i in range(len(s)):
            digit = ord(s[i])
            if (digit>96 and digit<123) or  (digit >= 48 and digit<=57 ):
                result+=s[i]
        
        i = 0 
        j = len(result)-1
        while(i < j ):
            if result[i] != result[j]:
                return False 
            i+=1
            j-=1
        return True
        