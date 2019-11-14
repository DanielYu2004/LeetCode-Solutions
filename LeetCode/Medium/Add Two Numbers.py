
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        l1_list = []
        l2_list = []
        digits = 0
        
        
        def listify(linkedlist, listedlinkedlist):
            if linkedlist.next:
                listedlinkedlist.append(linkedlist.val)
                global digits = global digits + 1
                listify(linkedlist.next, listedlinkedlist)
            else:
                listedlinkedlist.append(linkedlist.val)
                global digits += 1
                print(digits)
                
                
                
        listify(l1,l1_list)
        listify(l2,l2_list)

        #print(l1_list)
        #print(l2_list)



        
        


        
