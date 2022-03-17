class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = dict()
        for i in nums:
            try:
                hashmap[i]+=1
            except:
                hashmap[i]=1
        start = 0 
        end = len(nums)-1
        while start<=end:
            if hashmap[nums[start]]>1:
                hashmap[nums[start]]-=1
                check=nums.pop(start)
                nums.append(check)
                end-=1
            else:
                start+=1
        return start
            
            