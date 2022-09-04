# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        result = []
        
        op = new = ListNode(0)
            
        while head:

            result.append(head.val)

            head = head.next
                
        for x in range(0, len(result) - 1, 2):
            
            result[x], result[x+1] = result[x+1], result[x]
            
        for x in result:
            
            new.next = ListNode(x)
            new = new.next
            
        return op.next
