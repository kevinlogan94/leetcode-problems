# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)

# The following are not valid abbreviations:

# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)

# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

# A substring is a contiguous non-empty sequence of characters within a string.

# --------------------


# paramater - word: str, abbr:str
# Return - bool

# Q - 

# help
# h2p

# help
# he2

#    dec variables - num, wrdpntr, abbrpntr
# 1. loop through our abbr and word until we hit end
# 2.   if char is digit and start with 0 return false
# 3.      else is digit
# 4.         build out num until we hit char then increment word
# 5.   if word char != abbr char
# 6.     return false
# 7. return wrdpntr == word.length and abbrpntr == abbr.length 

# Space - O(1) 
# Time - O(n)

class Solution:
    def valid_abbr(self, word: str, abbr: str) -> bool:
        abbrpntr = wrdpntr = num = 0

        while abbrpntr < len(abbr) and wrdpntr < len(word):
            while abbrpntr < abbr[abbrpntr] and abbr[abbrpntr].isdigit():
                if abbr[abbrpntr] == "0" and num == 0:
                    return False
                num = num * 10 + int(abbr[abbrpntr])
                abbrpntr += 1
            wrdpntr += num
            num = 0
            
            if abbrpntr >= len(abbr) or wrdpntr >= len(word):
                continue

            if word[wrdpntr] != abbr[abbrpntr]:
                return False
            
            wrdpntr += 1
            abbrpntr += 1

        return abbrpntr == len(abbr) and wrdpntr == len(word)


# Variant

# The length does not have leading 0s and there is a wildcard substring.

# asdfg
# a1d*g

# if end return true
# keep incrementing g until we hit our value

class Solution:
    def valid_abbr_with_wildcard(word: str, abbr: str) -> bool:
        wrdpntr = abbrpntr = num = 0

        while wrdpntr < len(word) and abbrpntr < len(abbr):
            if abbr[abbrpntr] == "*":
                if abbrpntr == len(abbr) - 1:
                    return True
                else:
                    abbrpntr += 1
                    charToCheck = abbr[abbrpntr]

                    while charToCheck != word[wrdpntr] and wrdpntr < len(word):
                        wrdpntr += 1

            while abbr[abbrpntr].isdigit() and abbrpntr < len(abbr):
                num = num * 10 + int(abbr[abbrpntr])
                abbrpntr += 1
            
            wrdpntr += num
            num = 0

            if wrdpntr >= len(word) or abbrpntr >= len(abbr):
                continue

            abbrpntr += 1
            wrdpntr += 1

        return wrdpntr == len(word) and abbrpntr == len(abbr)