class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
    
        if (len(digits) == 0):
            return

        phone = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        output = list(phone[digits[0]]) 
        
        for digit in digits[1:]:
            temp = []
            for x in output:
                for y in list(phone[digit]):
                    temp.append(x+y)
            output = temp
                    
        return output
    
    
