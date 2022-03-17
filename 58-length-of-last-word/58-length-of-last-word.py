class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.rstrip().split(' ')[-1]
        return len(last_word)