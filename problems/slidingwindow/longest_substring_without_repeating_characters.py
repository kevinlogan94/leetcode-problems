# Given a string s, find the length of the longest substring without duplicate characters.
# -------------------


# parameters - s: str
# return - length_of_longest_substring: int

# Q - s only contain characters
# Q - s can be empty

# afezf - 4
# asas - 2
# aaaa - 1
# belt - 4

# sliding window - set

# class
# method
#  declare - seen, left, right, longest
#  move right pointer to the right
#       keep moving right and updating longest until we hit a duplicate
#       move left pointer to the right
#           keep comparing seen until we can advance again
# return longer


# Time - O(n) - n = len(s)
# Space - O(n) - n = len(s)

# afezf
# longest = 4
# left = 2, right = 4
# seen = [e,z]

class Solution:
    def longest_substring(self, s: str) -> int:
        seen = set()
        longest = left = right = 0
        end = len(s) - 1

        while right <= end:
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            length = right - left + 1
            longest = max(longest, length)

            right += 1

        
        return longest