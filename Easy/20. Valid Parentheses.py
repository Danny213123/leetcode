class Solution:
    def isValid(self, s: str) -> bool:
        
        while True:
            if (len(s) == 0):
                return True
            elif ("()" in s or "[]" in s or "{}" in s):
                s = s.replace("()", "")
                s = s.replace("[]", "")
                s = s.replace("{}", "")
            else:
                return False
        
        print(s)
