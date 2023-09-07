class Solution(object):
    def isIsomorphic(self, s, t):
        if ( len(s) != len(t)):
            return False
        map1 = {}
        map2 = {}
        for i in range(len(s)):
            if s[i] not in map1.keys()  :
                map1[s[i]] = t[i]
                
            elif map1[s[i]] != t[i] :
                return False 
            if  t[i] not in map2.keys():
                map2[t[i]] = s[i]
            elif (map2[t[i]] != s[i]):
                return False
                
        return True
                