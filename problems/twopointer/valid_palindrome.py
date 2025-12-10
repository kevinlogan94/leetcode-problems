# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# -------------------------

# parameters - s: str
# return - can_be_palindrome: bool

# Q - s can be empty


# s == s[::-1]
# racecar

# raceacar


# loop to the center with double pointers
#    if left and right pointer don't match
#       check if valid palindrome with left pointer char gone or right pointer char gone.
#           if so, return True otherwise False

# time - O(n)
# space - O(1)

class Solution:
    def valid_palindrome(self, s: str) -> bool: # O(n) -> n/2 -> n
        def check_palindrome(pntr: int) -> bool:
            new_s = s[pntr:] + s[:pntr + 1] # O(N) time complexity

            return new_s == new_s[::-1] # O(n) time compelexity
        
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return check_palindrome(left) or check_palindrome(right)
            left += 1
            right -= 1

        return True
    

# Variant - Remove at most k removals


# method(str, k)
#  define left, right
#  loop inwards
#    left, right don't match
#       if k > 0
#         k-1
#         left_s = removal of left
#         right_s = remove of right
#         return run_left or run_right
#       else return false
#    return true


# time - O(n)
# space - O(n)

class Solution:
    def valid_palindrome(self, s: str, k: int) -> bool:
        def _check_palindrome(left: int, right: int, k: int) -> bool:
            while left <= right:
                if s[left] != s[right]:
                    if k > 0:
                        return _check_palindrome(left+1, right, k-1) or _check_palindrome(left, right-1, k-1)
                    return False
                left += 1
                right -= 1
            return True
        
        left = 0
        right = len(s) - 1

        return _check_palindrome(left, right, k)

