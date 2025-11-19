# Given a string containing just the characters
#  '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

# --------------------

# parameters - string: str
# return - length_of_longest_substring: int

# Q - ( and )
# Q - can we have nothing be passed? yes


# stack - [index]
# index - index in stack
# (())))

# )((((())
# )))(((())))

# declare variables - > max = 0, stack = []
# loop through our array string
#    on ( -> append to our stack the index
#    on ) -> if stack -> run a max on the current index vs. last index in our stack. 
# return max

# Time - O(n) - n is the length of our string
# Space - O(n) - n is the length of our string



# "((()))(("
# "()()"

# "()()"
# "())()"

# [2] 4
# max - 2
# 
class Solution:
    def longest_valid_parenthesis_substring_length(self, string: Optional[str]) -> int:
        stack = [-1]
        max_length = 0

        if not string:
            return max_length

        for index, char in enumerate(string):
            if char == "(":
                stack.append(index)
            else:
                stack.pop()
                
                if not stack:
                    # This ')' is unmatched, it becomes the new boundary.
                    stack.append(index)
                else:
                    # This ')' is matched. Calculate length from the last unmatched boundary.
                    curr_length = index - stack[-1]
                    max_length = max(max_length, curr_length)

        return max_length
