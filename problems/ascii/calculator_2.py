# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# --------------------------------------

# parameters: s: str, 
# return: value: float

# "1 + 1"
# "2+1*3"
# "2+1-1*2/3"

# Q - negative values valid
# Q - +- */

# array of operations []
# loop through our string
#  if digit - build out our num
#  if operator - 
#    switch -
#      + - add the num to our operators array
#      - - set the num as negative, then add the num to our operators array
#      * - multiply the last value in our operator by the num
#      / - divide the last value in our operator by the num - be mindful of dividing in python
# return sum(operators)

# Time - O(n) n = the length of s
# Space - O(n) n = the length of s

class Solution:
    def calculator(self, s: str) -> float:
        operators = []
        num = 0
        operation = "+"
        s += "+" # Append a dummy operator to process the last number

        for char in s:
            if char.isspace():
                continue

            if char.isdigit():
                num = num * 10 + int(char)
            else:
                match operation:
                    case "+":
                        operators.append(num)
                    case "-":
                        operators.append(-num)
                    case "*":
                        operators[-1] *= num
                    case "/":
                        # Handle truncation toward zero for negative numbers
                        operators[-1] = int(operators[-1] / num)
                num = 0
                operation = char

        return sum(operators)





# Variant
# Same problem but only + and *

class Solution:
    def calculator(self, s: str) -> int:
        operators = []
        num = 0
        operation = "+"
        s += "+"

        for char in s:
            if char == "":
                continue
            elif char.isdigit():
                num = num * 10 + int(char)
            else:
                match operation:
                    case "+":
                        operators.append(num)
                    case "*":
                        operators[-1] *= num
                num = 0
                operation = char
            
        return sum(operators)