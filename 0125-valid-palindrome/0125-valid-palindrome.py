class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        while(i < j ):
            a = s[i].lower()
            b = s[j].lower()
            if not((97<=ord(a)<=122) or (48<=ord(a)<=57)):
                i+=1
                continue
            if not((97<=ord(b)<=122) or (48<=ord(b)<=57)):
                j-=1
                continue
            if (a == b):
                i+=1
                j-=1
                continue
            return False
        return True
                
        