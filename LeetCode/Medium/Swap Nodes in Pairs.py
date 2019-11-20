# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
		    return head
        if not head.next:
			return head
        
        pointer = head.next
        head.next = self.swapPairs(head.next.next)
        pointer.next = head
        return pointer
