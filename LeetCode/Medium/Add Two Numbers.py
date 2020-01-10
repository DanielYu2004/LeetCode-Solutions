# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        
        def add(l1,l2, carry, prevnode):
            if l1 or l2 or carry:
                if l1:
                    carry += l1.val
                    l1next = l1.next
                else:
                    l1next = None
                if l2: 
                    carry +=l2.val
                    l2next = l2.next
                else:
                    l2next = None
                    
                tempsum = carry % 10
                if carry > 9:
                    carry = 1
                else: 
                    carry = 0
                prevnode.next = ListNode(tempsum)
                add(l1next, l2next,carry, prevnode.next)
                return()
                
        temp = ListNode(None)
        add(l1,l2, 0, temp)
        return(temp.next)
                    