from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            M,N =0,0
        else:
            M, N = len(matrix), len(matrix[0])
        # 在二维数组的行，列前加一个空元素，可以避免数组越界的问题，只是在最后算值时，注意下标
        self.sumMN = [[0] * (N+1) for _ in range(M+1)]

        for i in range(M):
            for j in range(N):
                self.sumMN[i+1][j+1] = self.sumMN[i+1][j] + self.sumMN[i][j+1] - self.sumMN[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumMN[row2+1][col2+1] - self.sumMN[row2+1][col1] - self.sumMN[row1][col2+1] + self.sumMN[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)