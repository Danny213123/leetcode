class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        
        #[3,2,2,3]
        
        for i in range(0, len(nums)):
            if (nums[i] != val):
                temp = nums[i]
                nums[count] = temp
                nums[i] = temp
                count += 1
        return count
                
