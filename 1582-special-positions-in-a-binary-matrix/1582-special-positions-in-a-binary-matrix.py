class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        row = len(mat)
        column = len(mat[0])
        rows = [0]*row
        columns = [0]*column
        
        count = 0 
        for i in range(row):
            for j in range(column):
                if (mat[i][j] == 1):
                    rows[i]+=1
                    columns[j]+=1
                    
        for i in range(row):
            for j in range(column):
                if (mat[i][j] == 1 and rows[i] ==1 and columns[j] ==1 ):
                     
                        count+=1
                
        return count
                