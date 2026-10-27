#20261021

#答案
class Solution:

  def totalNQueens(self, n: int) -> int:
    self.count = 0

    def backtrack(row, col, diag1, diag2):
      # 如果行数达到了 n，说明找到了一种完整的合法摆放方案
      if row == n:
        self.count += 1
        return

      # 1. 找出当前行所有可以放置皇后的位置
      available_positions = (~(col | diag1 | diag2)) & ((1 << n) - 1)

      #col | diag1 | diag2找到至少有一个冲突的地方，1为冲突，~(col | diag1 | diag2)为一个冲突都没有的地方
      #但是取反会导致原数的一堆前导0变成前导1，需要去除，((1 << n) - 1) 是只有低位为1，前面有很多前导0的，用于截断

      # 2. 依次尝试当前行的每一个合法位置
      while available_positions:
        # 取出最低位的 1
        p = available_positions & -available_positions
        # 从可用位置中移除当前尝试的位置
        available_positions ^= p

        # 递归进入下一行，更新列和对角线状态
        backtrack(row + 1, col | p, (diag1 | p) << 1, (diag2 | p) >> 1)

    backtrack(0, 0, 0, 0)
    return self.count
  
