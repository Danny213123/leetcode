# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        result = []
        
        op = new = ListNode(0)
        
        for x in lists:
            
            while x:
                
                result.append(x.val)
                
                x = x.next
                
        for x in sorted(result):
            
            new.next = ListNode(x)
            new = new.next
            
        return op.next
