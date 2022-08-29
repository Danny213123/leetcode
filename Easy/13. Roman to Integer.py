class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D":500, "M":1000}
        
        
        num = 0
        
        
        for x in range(len(s)):
            if x + 1 < len(s) and roman[s[x]] < roman[s[x + 1]]:
                num -= roman[s[x]];
            else : 
                num += roman[s[x]];
        return num;
            
        
            
