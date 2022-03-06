class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        freq = [False]*58
        for i in jewels:
            freq[ord(i) - 65] = True
        for i in stones:
            if(freq[ord(i)-65]): count+=1
        return count