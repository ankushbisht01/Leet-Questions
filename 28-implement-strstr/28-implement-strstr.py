class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        total_char = len(needle)
        if  total_char==0:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+total_char] == needle:
                return i
        return -1