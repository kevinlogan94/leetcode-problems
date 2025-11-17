# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# -------------------------


# parameters - s: str
# return - valid: bool

# stack

# loop through s
#  if open (
#   add char to stack
#  if ])}
#    if stack is empty -> return False
#    else
#       latest stack item corresponds to char, pop it. Else return False

# at the end, if stack is empty return true

# {
#   "}":"{" 
# }

# Time - O(n) -> n the length of s
# Space - O(n) -> our stack could grow to be the length of n

class solution:
    def valid_parenthesis(self, s: str) -> bool:

        mapp = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if mapp[char] == stack[-1]:
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0