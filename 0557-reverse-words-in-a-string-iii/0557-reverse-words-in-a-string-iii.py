class Solution(object):
    def reverseWords(self, s):
        result = ""
        reverse = ""
        curr = 0 
        length = len(s)
        
        while(curr < length):
            if (s[curr]==" "):
                result= result+reverse+" "
                reverse = ""
            else:
                reverse = s[curr] + reverse
            curr+=1
        return result+reverse
        