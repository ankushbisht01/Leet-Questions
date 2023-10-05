class Solution(object):
    def majorityElement(self, nums):
        counts = dict()
        result = list()
        length = len(nums)
        for i in nums:
            if i in counts.keys():
                counts[i]+=1
            else:
                counts[i]=1
        
        for i , j in counts.items():
            if j > length /3 :
                result.append(i)
        return result