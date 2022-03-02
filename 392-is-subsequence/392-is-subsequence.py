class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        check = 0 
        for i in s:
            if i in t:
                count = t.find(i)+1
                t = t[count:]
            else:
                check = 1
                break 
        if check == 0 :
            return True
        else:
            return False