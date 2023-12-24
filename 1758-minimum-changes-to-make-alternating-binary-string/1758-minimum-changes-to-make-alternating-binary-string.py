class Solution:
    def minOperations(self, s: str) -> int:
        c1 = 0 
        c2 = 0 
        for i in range(len(s)):
            if s[i] != str(i%2):
                c1+=1
        for i in range(len(s)):
            if s[i] != str((i+1)%2):
                c2+=1
        return min(c1,c2)
            