# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] 
# (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the 
# probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).


# Constructor
# Parameter - arr: list[int]

# PickIndex
# parameter - no parameters 
# return - index NOT the value. 

# Pickindex must take into account the weight of the value to determine power how often the index comes back

# Q - arr values are 0-9
# Q - implement class with constructor and pickindex
# Q - No limit to the size of the array


# TC - [1,2]
# 1 / 3 = .33
# 2 / 3 = .77
# 

# [1,3]
# pickindex -> using rand.random(1,prefixsum[-1])

# [1,2,3]
# 

# prefix sum

# []


class Solution:

    def __init__(self, w: List[int]):
        self.range = 0
        self.ranges = []
        # Organize prefix sum
        for num in w:
            self.range += num
            self.ranges.append(self.range)

    def pickIndex(self) -> int:
        target = random.randint(1, self.ranges[-1])

        left = 0
        right = len(self.ranges) - 1

        best = 0

        while left <= right:
            mid = left + (right - left) // 2

            if self.ranges[mid] >= target:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return best
