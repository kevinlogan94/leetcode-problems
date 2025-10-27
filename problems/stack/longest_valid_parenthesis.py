# Given a string containing just the characters
#  '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

# --------------------

# parameters - chars: str
# return - max_length: int

# Q - is the string strictly "(())"
# Q - can the string be empty? Yes


# stack - 

# (((())
# ()
# stack = [-1]
# 1 + 1 = 2

# ())))()()
# stack = [4]
# 8 - 4 = 4

# stack - holds the latest boundary or left pointer


# Time - O(n)
# Space - O(n) n = len(chars)

# 1. def class
# 2. def method
# 3. def variables- stack[-1], max_length
# 4. loop through chars with enumerate
# 5.     if ( then append to stack
# 6.     if ), 
# 7             pop from stack
# 8.            if not stack -> append to stack
# 9             else: calculate our length and compare against max length

# "()"
# [-1]
class Solution:
    def valid_parenthesis(self, chars: str) -> int:
        stack = [-1]
        max_length = 0

        for index, char in enumerate(chars):
            if char == "(":
                stack.append(index)
            else:
                stack.pop()

                if not stack:
                    stack.append(index)
                else:
                    length = index - stack[-1]
                    max_length = max(max_length, length)

        return max_length