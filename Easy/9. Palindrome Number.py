class Solution:
    def isPalindrome(self, x: int) -> bool:
        k = str(x)
        d = k[::-1]
        
        if (k == d):
            return True
        else:
            return False
        
