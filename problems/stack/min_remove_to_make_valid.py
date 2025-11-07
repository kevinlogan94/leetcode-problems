# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

# ------------

# Parameters - s:str
# return - the final valid string: str


# return empty string if bad parenthesis

# valid
# asdf
# as()df

# invalid
# asd(f
# asdf))
# )(

# stack
# asd(f

# f(dsa
# a((sk)jd

# dj)ks(a
# 

# multiple ways
# create stack and set for )(

# build out the string left to right with a cntr
# loop through it in reverse order checking cntr
# return it in final order


# Time - O(n) n = len(s)
# Space - O(n) n = len(s)

# Solution with Variant(No Extra Space for Stack)


class Solution:
    def check_parenthesis(self, s: str) -> str:
        cntr = 0
        pass1 = []
        
        for char in s:
            if char.isalpha():
                pass1.append(char)
            elif char == "(":
                pass1.append(char)
                cntr += 1
            elif cntr > 0:
                pass1.append(char)
                cntr -= 1

        pass2 = []
        for char in pass1[::-1]:
            if char == "(" and cntr > 0:
                cntr -= 1
            else:
                pass2.append(char)

        return pass2[::-1]

        