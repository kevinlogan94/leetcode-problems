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


# parameters - word: str, abbr: str
# return - match: boolean

# Q - abbr is a str
# Q - can word be empty

# Don't forget leading 0.

# declare variables - abbr_cntr, word_cntr = 0 
#   num = 0

# loop through both abbr and word
#   check if abbr is num, if so loop through abbr until no longer num or we hit the end.
#     build upon num until end
#   add num to word_pntr
#   reset num

#   check if num or abbr are at or beyond the end, if so, continue
#   increment word_pntr and abbr_pntr

# return the comparison of word and abbr being equal to their pointers


# Time - O(n) n = length of abbr or word. Depends on the longer one
# Space - O(1)

class Solution:
    def match_abbr(self, word: str, abbr: str) -> bool:
        num = abbr_cntr = word_cntr = 0
        word_len = len(word)
        abbr_len = len(abbr)

        while abbr_cntr < abbr_len and word_cntr < word_len:
            
            while abbr_cntr < abbr_len and abbr[abbr_cntr].isdigit():
                digit = int(abbr[abbr_cntr])
                if num == 0 and digit == 0:
                    return False

                num = num * 10 + digit
                abbr_cntr += 1
            
            word_cntr += num
            num = 0

            if word_cntr >= word_len or abbr_cntr >= abbr_len:
                continue
             
            if word[word_cntr] != abbr[abbr_cntr]:
                return False

            abbr_cntr += 1
            word_cntr += 1
        
        return abbr_cntr == abbr_len and word_cntr == word_len


# Variant

# The length does not have leading 0s and there is a wildcard substring.

# asdfg
# a1d*g

# asdf*

# Q - Is this possible asd*1? 


class Solution:
    def match_abbr(self, abbr:str, word:str) -> bool:
        num = word_cntr = abbr_cntr = 0
        word_len = len(word)
        abbr_len = len(abbr)

        while word_cntr < word_len and abbr_cntr < abbr_len:

            if abbr[abbr_cntr] == "*":
                if abbr_cntr == abbr_len - 1:
                    return True
                
                while word_cntr < word_len and word[word_cntr] != abbr[abbr_cntr + 1]:
                    word_cntr += 1

            while abbr_cntr < abbr_len and abbr[abbr_cntr].isdigit():
                num = num * 10 + int(abbr[abbr_cntr])
                abbr_cntr += 1
            
            word_cntr += num
            num = 0

            if word_cntr >= word_len or abbr_cntr >= abbr_len:
                continue

            if word[word_cntr] != abbr[abbr_cntr]:
                return False
            
            abbr_cntr += 1
            word_cntr += 1
        
        return word_cntr == word_len and abbr_cntr == abbr_len