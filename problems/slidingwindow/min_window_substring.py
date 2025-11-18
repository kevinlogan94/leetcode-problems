# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring of s such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# -------------------------

# parameters - s:str, t:str
# return- min_substring_of_s: str

# HANDLE EDGE CASE

# sliding window

# s - asdft
# t - at

# s - astdfat
# t - att

# { a: 1, t: 2 }
# { a: 1, t: 2 }

# 1 define class
# 2 define method
# 3  cnt through t - t_map
# 4. declare variables - left, right, s_map, substring
# 5  loop through s
# 6.   move right until we have met requirements of t
# 7.     while requirements are met
# 8         move left pointer to the right and update substring
# 9. return "".join(substring)

# time - O(n) - n=length of s
# space - O(n) - n length of s

class solution:
    def substrings_of_s(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        sub_str = ""
        left = right = 0
        end = len(s) - 1
        s_map = {}
        t_map = {}

        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        
        need = len(t_map)
        have = 0

        while right <= end:

            char = s[right]
            if char in t_map:
                s_map[char] = s_map.get(char, 0) + 1
                if s_map[char] == t_map[char]:
                    have += 1
            
            while have == need and left <= right:
                if (right - left) < len(sub_str) or not sub_str:
                    sub_str = s[left:right + 1]

                char = s[left]
                if char in t_map:
                    s_map[char] -= 1
                    if s_map[char] < t_map[char]:                    
                        have -= 1
                left += 1

            right += 1

        return sub_str