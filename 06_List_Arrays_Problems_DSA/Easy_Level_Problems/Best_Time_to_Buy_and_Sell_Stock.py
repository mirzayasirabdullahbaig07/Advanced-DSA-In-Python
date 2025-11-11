"""
 LeetCode #121 — Best Time to Buy and Sell Stock

------------------------------------------------------------
 Problem Statement:
------------------------------------------------------------
You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.

You want to maximize your profit by choosing:
- A single day to **buy** one stock
- And a different day **in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

------------------------------------------------------------
 Example 1:
------------------------------------------------------------
Input:  prices = [7,1,5,3,6,4]
Output: 5
Explanation:
Buy on day 2 (price = 1) and sell on day 5 (price = 6)
Profit = 6 - 1 = 5

------------------------------------------------------------
 Example 2:
------------------------------------------------------------
Input:  prices = [7,6,4,3,1]
Output: 0
Explanation:
In this case, prices keep decreasing — no profit can be made.

------------------------------------------------------------
 Objective:
Find the **maximum difference** (sell_price - buy_price) such that:
- The buying day comes before the selling day.

------------------------------------------------------------
 Solution 1: Brute-Force Approach
------------------------------------------------------------
 Intuition:
Try every possible pair of days:
- Buy on day i
- Sell on any later day j (j > i)
Compute profit = prices[j] - prices[i]
Track and return the highest profit.

------------------------------------------------------------
 Code:
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] > prices[i]:
                    maxPro = max(maxPro, prices[j] - prices[i])
        return maxPro
"""
------------------------------------------------------------
 Dry Run:
prices = [7,1,5,3,6,4]
---------------------------------
i=0 → j runs 1..5:
    profits = [-, -6, -2, -4, -1, -3] → max = 0
i=1 → j runs 2..5:
    (5-1)=4, (3-1)=2, (6-1)=5, (4-1)=3 → max = 5
All later pairs give less → Final Answer = 5

------------------------------------------------------------
 Time Complexity:
O(n²) — two nested loops  
 Space Complexity:
O(1) — no extra space used

 Drawback:
Too slow for large inputs (up to 10⁵ prices).

------------------------------------------------------------
 Solution 2: Optimized Linear-Time Solution (Single Pass)
------------------------------------------------------------
 Intuition:
We don’t need to check every pair.
Instead:
- Keep track of the **minimum price so far** (best day to buy).
- For each new price, calculate potential profit = current_price - min_price.
- Update `max_profit` whenever this potential profit is larger.

------------------------------------------------------------
 Code:
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")     # start with very large number
        for price in prices:
            min_price = min(min_price, price)       # track lowest buying price
            max_profit = max(max_profit, price - min_price)  # check best profit
        return max_profit
"""
------------------------------------------------------------
 Step-by-Step Dry Run:
prices = [7, 1, 5, 3, 6, 4]

Initial:
min_price = ∞
max_profit = 0

Day | Price | min_price | profit (price - min_price) | max_profit
-------------------------------------------------
0   |   7   |    7       |     0 (7-7)               |    0
1   |   1   |    1       |     0 (1-1)               |    0
2   |   5   |    1       |     4 (5-1)               |    4
3   |   3   |    1       |     2 (3-1)               |    4
4   |   6   |    1       |     5 (6-1)               |    5 
5   |   4   |    1       |     3 (4-1)               |    5

Final Answer = 5  
(Buy at 1, Sell at 6)

------------------------------------------------------------
 Visualization:
Imagine stock prices as hills and valleys.
- We look for the **lowest valley** (best buy) before the **highest peak** (best sell).
- Keep scanning left → right while tracking these two values.

------------------------------------------------------------
 Time Complexity:
O(n) — single pass  
 Space Complexity:
O(1) — constant variables only

------------------------------------------------------------
 Comparison Summary:

| Approach        | Time   | Space | Logic                            | Efficiency |
|-----------------|--------|--------|----------------------------------|-------------|
| Brute Force     | O(n²)  | O(1)  | Compare all buy-sell pairs       |   Slow     |
| Optimized (1-pass) | O(n) | O(1)  | Track min price and max profit   |  Best     |

------------------------------------------------------------
 Final Notes:
The optimized approach is perfect for this problem:
- Runs in linear time
- Uses only two variables
- Elegant and intuitive

It’s one of the most common questions in interviews for testing algorithmic thinking and efficiency.
"""
