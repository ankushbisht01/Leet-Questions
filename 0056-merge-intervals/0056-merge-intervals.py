class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            last = result[-1]

            if last[1] >= intervals[i][0]:
                last[1] = max(intervals[i][1] , last[1])
            else:
                result.append(intervals[i])
        return result

        