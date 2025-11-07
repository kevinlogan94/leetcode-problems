# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


# Parameter - s: str
# return - bool

# Q - racecar -> racecar
# Q - aba -> aba

# ratcecar -> racectar

# Two pointer

# s == s[::-1]

# Time - O(n) n = len(s)
# Space - O(1)

class Solution:
    def valid_palindrome(self, s: str) -> bool:
        def _check_char_removal(index: int) -> bool:
            newstring = s[:index] + s[index + 1:]

            return newstring == newstring[::-1]

        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return _check_char_removal(left) or _check_char_removal(right)

            left += 1
            right -= 1

        return True
    


# Remove at most k removals


class Solution:
    def valid_palindrome(self, s: str, k: int) -> bool:
        def _check_palindrome(left:int, right:int, k:int) -> bool:
            while left <= right:
                if s[left] != s[right]:
                    if k <= 0:
                        return False
                    return _check_palindrome(left + 1, right, k-1) or _check_palindrome(left, right - 1, k-1)

                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        return _check_palindrome(left, right, k)