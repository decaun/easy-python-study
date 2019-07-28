'''
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def add_list_on_node(node, list, carry=0):
            node.val = (node.val+list.val+carry)
            carry = node.val//10
            node.val = node.val % 10
            if list.next:
                if node.next:
                    node.next = add_list_on_node(node.next, list.next, carry)
                else:
                    node.next = add_list_on_node(ListNode(0), list.next, carry)
            elif carry > 0 and node.next == None:
                node.next = add_list_on_node(ListNode(0), ListNode(0), carry)
            elif carry > 0 and list.next == None:
                node.next = add_list_on_node(node.next, ListNode(0), carry)
            return node

        node = ListNode(0)
        r = add_list_on_node(node, l1)
        r = add_list_on_node(r, l2)

        return r


'''
Runtime: 68 ms, faster than 64.70% of Python online submissions for Add Two Numbers.
Memory Usage: 12 MB, less than 5.16% of Python online submissions for Add Two Numbers.
'''
