from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            # ["NumArray","sumRange","sumRange","sumRange"]
            # [[[]]]
            self.nums = None
        elif len(nums) == 1:
            # ["NumArray","sumRange"]
            # [[[-1]],[0,0]]
            self.nums = nums
        else:
            self.cursor = nums[1]
            self.nums = nums
            for i in range(len(self.nums)):
                if i == 0:
                    self.nums[i] = self.nums[0]
                elif i == len(self.nums) - 1:
                    self.nums[i] += self.nums[i - 1]
                else:
                    self.cursor = self.nums[i + 1]
                    self.nums[i] += self.nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        if self.nums == None:
            return None
        if i==0:
            return self.nums[j]
        else:
            return self.nums[j] - self.nums[i-1]

# Your NumArray object will be instantiated and called as such:
nums = [-1]
obj = NumArray(nums)
i = 0
j = 0
param_1 = obj.sumRange(i,j)