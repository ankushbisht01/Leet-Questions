class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length = len(s)
        if length == 0 or length == 1:
            return length

        elements = set()

        l = 0 
        max_length = 0 

        for r in range(length):
            while s[r] in elements:
                elements.remove(s[l])
                l+=1
            elements.add(s[r])
            max_length = max(max_length, r-l+1)
        return max_length
            

