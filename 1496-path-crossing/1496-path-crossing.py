class Solution:
    def isPathCrossing(self, path: str) -> bool:
        checked = set()
        checked.add((0,0))
        x = 0 
        y = 0 
        for i in path:
            if i == "N":
                y+=1
            elif i == "S":
                y-=1
            elif i == "E":
                x += 1
            else:
                x-=1
            if (x,y) in checked:
                return True
            checked.add((x,y))
        return False