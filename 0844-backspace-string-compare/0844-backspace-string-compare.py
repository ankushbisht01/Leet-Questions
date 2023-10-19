class Solution(object):
    def backspaceCompare(self, s, t):
        top1=0 
        top2 = 0 
        s1 = []
        s2 = []
        for i in range(len(s)):
            if s[i] == "#":
                if len(s1)!=0:
                    s1.pop()
            else:
                s1.append(s[i])
        
        for i in range(len(t)):
            if t[i] == "#":
                if len(s2)!=0:
                    s2.pop()
            else:
                s2.append(t[i])
        
        if len(s1)!= len(s2):
            return False
        
        for i in range(len(s1)):
            if s1.pop() != s2.pop():
                return False
        return True