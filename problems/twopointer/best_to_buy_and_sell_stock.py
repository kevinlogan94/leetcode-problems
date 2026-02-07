# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# ----------------------

# parameters - prices: List[int]
# return - max_profit: int

# Q - the prices are ints
# Q - prices can't be empty

# [1,2,3,4]
# buy low and sell high

# [6,3,9,1]
# [1,8,4,9]

# class
# method
#  loop through prices from right to left
#     check if num is higher the highest num
#        if so, update highest num otherwise compare new potential max profit
#  return final max profit


# O(n) - n = len(prices)
# O(1)

class Solution:
    def buy_sell_stocks(self, prices: List[int]) -> int:
        sell = prices[-1]
        max_profit = 0

        pntr = len(prices) - 2
        while pntr >= 0:
            if prices[pntr] > sell:
                sell = prices[pntr]
            else:
                profit = sell - prices[pntr]
                max_profit = max(max_profit, profit)
            pntr -= 1
        
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