class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False 
        occ = dict()
        for i in s:
            if i in occ.keys():
                occ[i]+=1
            else:
                occ[i]=1
        for i in t:
            if ( i not in occ.keys() ):
                return False
            if occ[i] == 0 :
                return False
            else:
                occ[i]-=1
        return True
            