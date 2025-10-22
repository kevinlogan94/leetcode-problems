# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# parameter of s: str
# return a boolean

# palindrome? - racecar
# racecar

# Q - yes always characters
# Q - empty string - yes
# Q - racecar - return true

# tc - racecar
# tc - raceca2r
# tc - ""
# tc - ratcectar

# Two pointer

# 1.
# loop through our palindrome s
# two pointers - 1 at the beginning, 1 at the end
# loop until they collide in the middle

# 2.
# if pointers don't match, we would run a submethod to compare

# 3.
# break up our string around the index and check if it's a palindrome
# submethod - index : bool
#   newstring = [::]
#   return newstring[::-1] == newstring

# Time - O(n)
# Space - O(1)

class Solution:
    def palindrome(self, string: str) -> bool:
        def _compare(index: int) -> bool:
            newstring = string[:index] + string[index+1:]
            return newstring[::-1] == newstring
    
        left = 0
        right = len(string) - 1

        while left <= right:
            if string[left] != string[right]:
                return _compare(left) or _compare(right)
        
            left += 1
            right -= 1
        
        return True