# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = new = ListNode(0)
        d = []
        
        while head:
            
            d.append(head.val)
            head = head.next
            
        d.pop(len(d) - n)
        
        for x in (d):
            
            new.next = ListNode(x)
            new = new.next
            
        return temp.next
            
