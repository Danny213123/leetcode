class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        time = nums
        time.sort()
        
        closest, diff = 0, 9999
        
        for x in range (len(time) - 2):
            
            left, right = x + 1, len(time) - 1
            
            first = time[x]
            
            while left < right:
                
                total = first + time[left] + time[right]
                
                if (abs(target - total) < diff):
                    
                    diff, closest = abs(target-total), total
                    
                elif (total > target):
                    
                    right -= 1
                    
                else:
                    
                    left += 1
                        
        return closest
