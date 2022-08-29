# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()
        dum = l3
        list1, list2 = [], []
        carry = 0
        
        while l1 or l2 or int(carry):
            
            # check node 1 and node 2 have values, otherwise return 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # add values from node 1 and node 2 to lists
            list1.append(val1) if val1 else 0
            list2.append(val2) if val2 else 0
            
            # check to see if total value is greater than 10
            val = val1 + val2 + carry
            carry = int(val / 10)
            val = int(val % 10)
            
            # add to listnode.next
            dum.next = ListNode(val)
            
            # move 1 node forward
            dum = dum.next
            
            # check if l1 and l2 next node is empty
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        #return listnode, skip first node which was allocated in memory
        return l3.next
