# word, abbr
# word = "smart" abbr = "s3t"
# double pointer approach
# return bool
# Contains only lowercase letters
# can't be empty

# lol l1l
# O(n) - Time Complexity
# O(1) - Space Complexity

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordpntr = abbrpntr = abbrnum = 0

        while wordpntr < len(word) and abbrpntr < len(abbr):
            while abbrpntr < len(abbr) and abbr[abbrpntr].isdigit():
                if abbr[abbrpntr] == '0' and abbrnum == 0:
                    return False
                abbrnum = abbrnum * 10 + int(abbr[abbrpntr])
                abbrpntr += 1

            wordpntr += abbrnum
            abbrnum = 0

            if wordpntr >= len(word) or abbrpntr >= len(abbr):
                continue

            if abbr[abbrpntr] != word[wordpntr]:
                return False

            wordpntr += 1
            abbrpntr += 1

        return wordpntr == len(word) and abbrpntr == len(abbr)
       