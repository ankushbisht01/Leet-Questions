class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0 
        hashmap = dict()
        for i in nums:
            if i in hashmap.keys():
                hashmap[i]+=1
            else:
                hashmap[i]=1
        
        for i in nums:
            count += hashmap[i]-1
            hashmap[i]-=1
        return count
  