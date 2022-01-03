class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = 0
        b=[]
        for i in rectangles:
            b.append(min(i))
        max_side = max(b)
        for i in rectangles:
            print(max_side,i[0],i[1])
            if max_side <= i[0] and max_side <= i[1]:
                count+=1
        return count
                