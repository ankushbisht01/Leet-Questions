class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result = 0
        for i in range(len(s)-1):
            if romans[s[i]]<romans[s[i+1]]:
                result = result - romans[s[i]]
            else:
                result = result + romans[s[i]]
        return result+romans[s[-1]]