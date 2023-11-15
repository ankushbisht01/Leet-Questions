class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0]=1
        max_elem = 1 
        for i in range(1, len(arr)):
            if not(arr[i] - arr[i-1] <= 1):
                arr[i] = arr[i-1]+1
            if(arr[i] > max_elem):
                max_elem = arr[i]
        return max_elem
                