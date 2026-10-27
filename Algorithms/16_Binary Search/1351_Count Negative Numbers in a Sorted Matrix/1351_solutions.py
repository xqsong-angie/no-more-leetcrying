#20261022

#答案，这道题严格来讲不算二分
class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        row = 0
        col = cols - 1  # 从右上角开始
        count = 0
        
        while row < rows and col >= 0:
            if grid[row][col] < 0:
                # 如果当前是负数，那么它下方的所有数（当前列的剩余行）也全是负数
                count += (rows - row)
                # 这一列已经统计完了，往左移动一列
                col -= 1
            else:
                # 如果当前数大于等于0，说明当前位置太大了，往下移动一行去找负数
                row += 1
                
        return count