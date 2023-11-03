class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]: 
        stream = 1
        result = []
        while(stream <= target[len(target)-1]):
            if stream in target:
                result.append("Push")
            else:
                result.append("Push")
                result.append("Pop")
            
            stream+=1
        return result 
                