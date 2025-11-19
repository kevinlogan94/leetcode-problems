# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# ----------------------

# parameters - stocks: int
# return max_profit_value: int

# Sliding window

# buy low and sell high

# left, right = 0

# move right till right > left -> calc max
# then move left until left >= right


# O(n) - n = len(stocks)
# O(1)


# [3,4,1]
# [1,3,4,5,3,10]
# [1,2,10,5,4]
class Solution:
    def buy_and_sell_stocks(self, stocks: List[int]) -> int:
        max_profit = 0
        end = len(stocks) - 1
        left = right = end


        while left >= 0:

            profit = stocks[right] - stocks[left]
            if profit < 0:
                right = left
            else:
                max_profit = max(max_profit, profit)
            left -= 1
        
        return max_profit
    

# Variant - Cheapest Roundtrip Flight

# You are given two arrays `departure` and `arrival` where `departure[i]` and `arrival[i]` represent the departure and return prices of a flight on the ith day.

# You want to minimize your cost by choosing a single day to depart and a different day in the future to return.

# Return the minimum cost you can achieve from a single roundtrip flight.

# ----------------------

# parameters: departure: List[float], arrival: List[float]
# return - min_cost: float

#          -
# [3,2,1,4,5]
#  -        
# [2,3,4,5,6]

#          -
# [2,4,3,2,1]
#  _
# [1,9,3,5,6]

# Time - O(n)
# Space - O(1)

# loop through our arrivals
#  start at 1, start dep at 2
#  loop through and keep calculating the min value
# 

class Solution:
    def rountrip_flight(self, departure:List[float], arrival: List[float]) -> float:
        min_cost = float("inf")
        min_depart = departure[0]

        for i in range(1, len(arrival)):
            min_depart = min(min_depart, departure[i-1])
            new_cost = min_depart + arrival[i]
            min_cost = min(min_cost, new_cost)

        return min_cost