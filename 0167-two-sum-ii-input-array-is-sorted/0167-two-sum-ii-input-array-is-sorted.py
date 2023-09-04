class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0 
        sum = 0 
        j = len(numbers)-1
        
        while(i < j ):
            sum = numbers[i] + numbers[j]
            if (sum == target):
                return [i+1,j+1]
            if(sum < target):
                i+=1
            else :
                j-=1
        return []
        