# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

# string s as a parameter
# Return a valid string
# valid? 

# Q - "asdf" - yes
# Q - "" - yes
# Q - "()" - yes
# Q - "))(" - No -> ""
# Q - "a)s(df)" - No -> "ad(df)"

# Stack - LiFo - [1] - []

# 1.
# loop through s
# skip our characters
# Stack will help us know what ( we need to remove
# if ) - check stack - append remove array 
# remove array tells us what ) to remove

# 2.
# Stack and remove array
# extend - stack.append(remove)

# 3.
# result = []
# loop through our string
# if index that is stack or remove array
#  then we want ignore it.

# stack - []
# remove - [1]
# "a)s(df)"

# stack - [2]
# remove - [0, 1]
# "))("

# time complexity - o(n)
# space complexity - o(n)

class Solution:
    def minnumtoremove(self, string:str) -> str:
        stack = []
        remove = []

        # 1.
        for index, char in enumerate(string):
            if char.isalpha():
                continue
            if char == "(":
                stack.append(index)
            else:
                if not stack:
                    remove.append(index)
                else:
                    stack.pop()
        # 2.
        stack.extend(remove)
            
        # 3.
        res = []
        for index, char in enumerate(string):
            if not index in stack:
                res.append(char)

        return "".join(res) 