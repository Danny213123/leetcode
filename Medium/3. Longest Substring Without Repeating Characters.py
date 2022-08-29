class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_list = set()
        num_substrings = 0
        length = 0
        
        # run through length of s
        for x in range (len(s)):
            
            # check if s[x] is in set (s); set contains unique characters in s
            while (s[x] in s_list):
                
                # if s[x] is in set, remove the character from s
                s_list.remove(s[num_substrings])
                
                num_substrings += 1
                
            # add s[x] into set    
            s_list.add(s[x])
            
            length = max(length, x - num_substrings + 1)
            
        return length
