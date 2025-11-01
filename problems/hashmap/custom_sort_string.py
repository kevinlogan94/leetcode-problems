# You are given two strings order and s. All the characters of order are unique and were 
# sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, 
# if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

# --------------------------

# parameter - order: str, s: str
# return - permutation of s

# Q - Order chars are not in s

# two pointer problem

# {}
# {a: 1, d: 1, f: 2}
# order = "af"
# s = "dffa"
# return "jfasdf"

# Time - O(n) = len(s)
# space - O(n) = len(s)

# 1. define class
# 2. define method
# 3.  build out counts of s
# 4.  loop through order
# 5.    compare orderitem to countsOfs, append orderitem countOfs times and pop property
# 6.  loop through countOfs and append lingering items
# 7.  return array joined together

class Solution:
    def custom_sort(self, s: str, order: str) -> str:
        new_s = []
        count_of_s = {}

        for char in s:
            count_of_s[char] = count_of_s.get(char, 0) + 1
        
        for char in order:
            if not char in count_of_s:
                continue
            counts = count_of_s[char]
            new_s.append(char * counts)
            count_of_s.pop(char)
        
        for char, counts in count_of_s.items():
            new_s.append(char * counts)
            
        return "".join(new_s)