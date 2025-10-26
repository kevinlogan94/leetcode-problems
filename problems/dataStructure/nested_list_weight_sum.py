# You are given a nested list of integers nestedList. Each element is either an integer 
# or a list whose elements may also be integers or other lists.

# The depth of an integer is the number of lists that it is inside of. For example, 
# the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

# Return the sum of each integer in nestedList multiplied by its depth.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


# ------------------------------------

# Parameter - nestedList: List[]
# Return - sum: int

# Q - int can't be negative
# Q - list could be len of inf
# Q - depth starts at 1

# [1, [2,[3,3,[4]]]]
# [1, 4, 9, 9, 16] - parts

# return sum(parts)

# isinstance(numorlist, list)
# isinstance(numorlist, int)

# Time - O(n) - n = the total amount of elements in our nested list.
# Space - O(n) - n = the total amount of elements in our nested list. 

# 1 class solution
# 2 def method
# 3. loop through list
# 4.   check type
# 5.     if int - add to our parts array
# 6.     if list - increment depth and repeat
# 7
# 8.  return sum(parts)

# [1, [2,[3,3,[4]]]]
# [1, 4, ]

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.parts = []

        def _checklist(nestedList: List, depth: int) -> None:
            for item in nestedList:
                if item.getInteger():
                    self.parts.append(item.getInteger() * depth)
                else:
                    _checklist(item.getList(), depth + 1)

        _checklist(nestedList, 1)

        return sum(self.parts)

