from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0. "def maxProfit(self, prices: List[int]) -> int:" is Function Annotation
        # (https://docs.python.org/3.5/tutorial/controlflow.html#function-annotations)

        # 1. min_price can't be 0, max_profit will be (max price - 0).  [7,1,5]->7
        # 2. min_price can't be prices[0], exception will be raised when prices is none
        # 3. float("inf") acts as an unbounded upper value for comparison.
        #    This is useful for finding lowest values for something.
        min_price, max_profit = float("inf"), 0

        if prices is None or len(prices) < 2:
            return 0

        for price in prices:
            # use built-in func like min(),max() instead of if statement
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)

        print(max_profit)
        return max_profit

prices = [1,2]
s = Solution()
s.maxProfit(prices)
