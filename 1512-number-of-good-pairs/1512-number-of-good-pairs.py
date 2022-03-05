class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0 
        frequency_array = [0]*101
        for i in nums:
            frequency_array[i]+=1
        
        for i in nums:
            count += frequency_array[i]-1
            frequency_array[i]-=1
        return count
  