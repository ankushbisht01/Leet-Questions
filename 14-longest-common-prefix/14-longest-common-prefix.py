class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        shortest , longest = min(strs),max(strs)
        for i in range(len(shortest)):
            if shortest[i]==longest[i]:
                result +=shortest[i]
            else:
                break
        return result