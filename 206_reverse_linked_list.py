'''
Reverse a singly linked list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        Traverse the linked list and change the node pointer, current_node.next = previous_node
        However, remember, before change the pointer, store current_node.next to the next_node
        '''
        current_node = head
        previous_node = None
        while current_node:
            # before change then current_node.next, store it in a variable called next_code
            next_node = current_node.next
            # chanage the pointer to previous node
            current_node.next = previous_node

            # move on to next node
            previous_node = current_node
            current_node = next_node

        head = previous_node
        return head
