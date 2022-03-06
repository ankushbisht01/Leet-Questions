class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = 0
        result = []
        for i in candies:
            if i > max_candies:
                max_candies = i
        for i in candies:
            if (i+extraCandies) >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result