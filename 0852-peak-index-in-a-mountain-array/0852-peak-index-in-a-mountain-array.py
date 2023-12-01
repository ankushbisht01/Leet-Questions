class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if (arr[0]  > arr[1]):
            return 0
        if (arr[len(arr)-1]  > arr[len(arr)-2]):
            return len(arr) 
        for i in range(1,len(arr)-1):
            if arr[i]> arr[i-1] and arr[i]>arr[i+1]:
                return i
        