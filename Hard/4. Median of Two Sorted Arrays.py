class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        List = (nums1 + nums2)
        List.sort()
            
        if (len(List) % 2 == 0):
            return ((List[len(List) // 2] + List[len(List) // 2 - 1]) / 2)
        else:
            return ((List[len(List) // 2]))
