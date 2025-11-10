# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] 
# (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the 
# probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

#  -------------------


# parameters - nums: List[int]
# implement - pickIndex
# return - int

# random.randint(0, len(nums) - 1)

# Q - no duplicates

# ranges
# [1,3,2,4]
# [1,4,6,10]

# [1,3]
# [1,4]

# random.randint(1, len(nums))
# binary search to start at mid - left bound binary search



# Space - O(n) - we choose the space complexity based on the high storage used in all our classes methods.
# Time - O(log n)


# [1,2,3]
# [1,3,6]
# 0, 2 with mid 1 and target 2 -> 0, 1 with mid 0 and target 2 -> 1, 1 with mid 1 and target 2 -> return 1
class Solution:

    def __init__(self, nums: List[int]):
        self.ranges = []
        self.range = 0
        for num in nums:
            self.range += num
            self.ranges.append(self.range)

    def pickindex(self) -> int:
        target = random.randint(1, self.range)

        left, right = 0, len(self.ranges) - 1

        while left < right:
            mid = left + (right - left) // 2

            if self.ranges[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left



# Variant #1 - City Populations
# What if you had to return the city that a person lives in? The input is given very differently.

# you are conducting an A/B split test and need to randomply pick a person from a user based spread scross multiple cities. 
# Each city has a known population, and you need to ensure that the probability of picking a person from a city is proportional 
# to the population of that city.

# you are given a 0-indexed array of pairs city_population, where each pair consists of a string representing the name of the ith 
# city and an integer representing the population of the ith city.

# you need to implement the function pickindex(), which randomly picks a person in and returns the name of the city the person is in.

# -------------------

# Parameters - city_population: List[Tuple[city: str, population: int]] 
# Returns - city_chosen: str

# [("A", 1), ("B", 3), ("C", 2)]
# City A -> 1/6
# City B -> 3/6
# City C -> 2/6


# ranges - [1,4,6] - random.randint(1, 6)

# binary search
# get index -> map back to our city
# return city_population[index][0]


# Time - O(log n)
# Space - O(n)

class Solution:
    def __init__(self, city_population: List[Tuple[str, int]]):
        self.range = 0
        self.ranges = []
        self.cp = city_population
        for _, population in city_population:
            self.range += population
            self.ranges.append(self.range)
    
    def pickindex(self) -> str:
        target = random.randint(1, self.range)

        left, right = 0, len(self.ranges) - 1

        while left < right:
            mid = left + (right - left) // 2

            if self.ranges[mid] < target:
                left = mid + 1
            else:
                right = mid

        result = self.cp.get(left, None)    
        return result[0] if result else None   
