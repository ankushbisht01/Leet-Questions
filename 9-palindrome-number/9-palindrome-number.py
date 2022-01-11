class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        else:
            b=x
            rev = 0
            while x > 0 :
                rem = x % 10
                rev = rev *10 + rem
                print(rev)
                x = x//10
            if rev != b:
                return False
            else :
                return True