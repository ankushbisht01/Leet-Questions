class Solution(object):
    def winnerOfGame(self, colors):
        if len(colors) < 3 :
            return False
        moves = {
            'A':0,
            'B':0
        }
        
        for i in range(1,len(colors)-1):
            if (colors[i] == colors[i-1] and colors[i] == colors[i+1]):
                moves[colors[i]] += 1
        
        if (moves['A'] > moves['B']):
            return True 
        return False 
        