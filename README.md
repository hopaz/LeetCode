# LeetCode
本项目的.py文件均在Pycharm中运行，编码时题目中涉及的类没有import，pycharm会划红线提示
“unresolved”，此时需要手动import这些类，但提交LeetCode时不需要这些import语句。

另外，LeetCode上点击提交的时候，实际上是将提交代码中的类实例化，调用该对象的方法，并
传入测试数据，给出结果。在Pycharm运行就需要手动实例化Solution对象，并调用相应的方法，
传入参数，运行得出结果。

例如：
[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

本项目代码在Pycharm中是这样的：
```python3
# To run file in pycharm, you need import some classes according to "unresolved error" prompt 
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # remove following notes before submit
        # 1. min_price can't be 0, max_profit will be (max price - 0).  [7,1,5]->7
        # 2. min_price can't be prices[0], exception will be raised when prices is none
        # 3. float("inf") acts as an unbounded upper value for comparison.
        #    This is useful for finding lowest values for something.
        min_price, max_profit = float("inf"), 0;

        if(prices is None or len(prices) < 2):
            return 0

        for price in prices:
            # use built-in func like min(),max() instead of if statement
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)

        # remove print statement before submit on leetcode
        print(max_profit)
        return max_profit

# remove init statement before submit
# test data
prices = [1,2]

# new object of Solution
s = Solution()

# run proper func for test
s.maxProfit(prices)
```

LeetCode提交的代码是这样的：
```python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int
    
        min_price, max_profit = float("inf"), 0;

        if(prices is None or len(prices) < 2):
            return 0

        for price in prices:
           min_price = min(price, min_price)
           max_profit = max(max_profit, price - min_price)

        return max_profit
```
