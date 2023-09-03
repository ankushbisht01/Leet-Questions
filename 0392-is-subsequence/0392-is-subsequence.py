class Solution(object):
    def isSubsequence(self, s, t):
        if (len(s)>len(t)):
            return False
        i = 0 
        j = 0
        
        while(i < len(s) and j < len(t)):
            if (s[i]==t[j]):
                i+=1
                j+=1
                continue
            j+=1
        if (i < len(s)):
            return False
        return True
         
        