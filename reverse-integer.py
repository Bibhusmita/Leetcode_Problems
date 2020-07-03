class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        n = 1
        if x < 0:
            n = -1
            x = abs(x)
        while x > 0:
            rev = rev * 10 + x % 10
            x = x//10
        if rev < 2**31:
            return rev*n
        else:
            return 0
            
        