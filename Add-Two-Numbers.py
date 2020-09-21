# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         looking for what is the first number
        num1 = 0
        i = 1
        val1 = l1
        while val1:
            num1 += i*val1.val
            i *= 10
            val1 = val1.next
            
#             looking for what is the second number
        num2 = 0
        i = 1
        val2 = l2
        while val2:
            num2 += i*val2.val
            i *= 10
            val2 = val2.next
        
#         adding two nums
        num_sum = num1 + num2
        
        
#         converting to the linked list
        list_num = [int(x) for x in str(num_sum)] 
        list_num.reverse()
        # print(list_num)
        new_node = ListNode()
        current_node = new_node
        for i in range(0, len(list_num)):
            current_node.val = list_num[i]
            if i == len(list_num)-1:
                current_node.next = None
            else:
                current_node.next = ListNode(list_num[i+1])
                current_node = current_node.next
        return new_node