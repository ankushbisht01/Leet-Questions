class Solution(object):
    def rotate(self, matrix):
        
        temp = []
        n = len(matrix)
        for i in range(n/2):
            temp = matrix[i]
            matrix[i] = matrix[n-i-1]
            matrix[n-i-1] = temp
        
        for i in range(n):
            for j in range(0 , i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        
        
            
        