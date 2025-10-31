# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring of s such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# -------------------------

# parameters - s: str, t: str
# return - min substring: str

# Q - S and t can be empty
# Q - s and t can both have duplicate characters
# Q - 

# sliding window
# hashmap - counts out the chars in t
# 

# 
# 1 loop through s
# 
# 2  if matchcount != len(hashmapt)
# 3   move right pointer until we have a substring with all values. Making our substring valid. if matchcount != len(hashmapt)
# 4     on each new loop, check new char if it is in hashmapt, increment value in hashmaps. 
# 5       If value in hashmapt == hashmaps. increment matchcount.
# 6     if matchcount == len(hashmapt):
# 7        update substring if less than existing substring 
# 8  else
# 9   move left pointer, until we have a substring that is invalid. match != len(hashmapt) or left >= right
# 10       update min substring
#       
# 
# 

# return our result

# Time - O(n) -> n = len(s)
# Space - O(n) -> n = len(t)

class Solution:
    def min_window(self, s:str, t:str) -> str:
        mapt = {}
        maps = {}
        substr = ""

        left = right = 0
        end = len(s) - 1

        if not s or not t:
            return substr
        
        for char in t:
            mapt[char] = mapt.get(char, 0) + 1

        have = 0
        need = len(mapt)
        
        while right <= end:
            char = s[right]
            maps[char] = maps.get(char, 0) + 1

            if char in mapt and maps[char] == mapt[char]:
                have += 1

            while have == need:
                if right - left + 1 < len(substr) or not substr:
                    new_substr = s[left:right + 1]
                    substr = new_substr
                
                char = s[left]
                maps[char] -= 1

                if char in mapt and maps[char] < mapt[char]:
                    have -= 1
                left += 1
            right += 1

        return substr