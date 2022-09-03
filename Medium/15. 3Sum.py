class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        time = nums
        time.sort()
        
        output = []
        
        for x in range (len(time) - 1):
            
            left, right = x + 1, len(time) - 1
            
            first = time[x]
            
            if (x == len(time) - 1):
                
                return
            
            while left < right:
                
                if (first + time[left] + time[right] < 0):
                    
                    left += 1
                    
                elif (first + time[left] + time[right] > 0):
                    
                    right -= 1
                    
                else:
                
                    if (first + time[left] + time[right] == 0):
                        
                        if ([first, time[left], time[right]] not in output):
                            
                            output.append ([first, time[left], time[right]])
                        
                        left += 1
                        
                        while (left < right) and nums[left] == nums[left - 1]:
                            
                            left += 1
                        
        return output
                
