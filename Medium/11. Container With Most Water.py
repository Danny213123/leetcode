class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_x= 0
        right_x = len(height)-1
        
        while left_x < right_x:
            
            width = right_x - left_x
            
            #print(height[right_x], height[left_x])
            
            max_height = min(height[right_x], height[left_x])
            
            if (width*max_height > max_area):
                
                max_area = width*min(height[right_x], height[left_x])
                
            if (height[left_x]<height[right_x]):
                
                left_x+=1
                
            else:
                
                right_x-=1
                
        return (max_area)
