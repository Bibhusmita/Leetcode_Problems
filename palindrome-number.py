class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            rev = 0
            n = x
            while x > 0:
                rev = rev*10 + x%10
                x = x//10
            if rev == n:
                return True
            else:
                return False
        