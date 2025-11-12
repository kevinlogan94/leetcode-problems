# You are given two non-empty linked lists representing two non-negative integers. The 
# digits are stored in reverse order, and each of their nodes contains a single digit. Add the two 
# numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# -----------------------------------

# parameters: nums1: ListNode, nums2: ListNode
# return: sum: ListNode

#  123
# + 12
#  135

#  129
# + 12 
#  141

# 3 2 1
# 2 1

# 9 2 1
# 4 1

# Carry pattern
# 0-9

# 13 // 10 -> 1. -> 1
# 13 % 10 -> 3
# 3

# loop through them left to right until we have used all vals and no carry left
#  carry = sum // 10 
#  val = sum % 10
#  add together to make new node with sum

# Time - O(n) n = len of the greater list + 1 because carry
# Space - O(1)


class Solution:
    def add_two_nums(self, num1: ListNode, num2: ListNode) -> ListNode:

        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while num1 or num2 or carry:
            val1 = num1.val if num1 else 0
            val2 = num2.val if num2 else 0 

            sum_val = val1 + val2 + carry

            carry = sum_val // 10
            val = sum_val % 10

            curr.next = ListNode(val)
            curr = curr.next

            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next
        
        return dummy.next

