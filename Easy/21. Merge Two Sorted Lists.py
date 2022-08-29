# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = [], []
        list3 = ListNode()
        dum = list3
        
        while list1:
            l1.append(list1.val)
            list1 = list1.next
            
        while list2:
            l2.append(list2.val)
            list2 = list2.next
            
        l3 = l1 + l2
        l3.sort()
        
        for x in range(len(l3)):
            dum.next = ListNode(l3[x])
            dum = dum.next
            
        return list3.next
        
            
