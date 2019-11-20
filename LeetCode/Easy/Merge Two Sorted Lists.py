# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        
        if not l1 and not l2:
            return(None)
        if not l1:
            return(l2)
        if not l2: 
            return(l1)
        
        pointer = None
        
        if  l1.val<=l2.val:
            pointer = l1
            pointer.next = self.mergeTwoLists(l1.next, l2) 
        else: 
            pointer = l2
            pointer.next = self.mergeTwoLists(l2.next, l1)
        return pointer
