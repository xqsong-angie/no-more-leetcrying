#20251021

#答案
class Solution:

  def solveNQueens(self, n: int) -> list[list[str]]:
    res = []
    # 用于记录每一行皇后所在的列号，方便最后转成题目要求的字符串格式
    queens = []

    def backtrack(row, col, diag1, diag2):
      # 如果行数达到了 n，说明找到了一个合法解
      if row == n:
        # 将结果转化为棋盘的字符串格式
        board = []
        for c in queens:
          board.append("." * c + "Q" + "." * (n - 1 - c))
        res.append(board)
        return

      # 1. 找出当前行所有可以放皇后的位置（为 1 的位）
      # ~(col | diag1 | diag2) 把冲突位置置为 0，可用位置置为 1
      # & ((1 << n) - 1) 用于截断多余的高位
      available_positions = (~(col | diag1 | diag2)) & ((1 << n) - 1)#🔥这里也还是没太看懂

      # 2. 循环遍历当前行所有可以放皇后的位置
      while available_positions:
        # 取出最低位的 1（贪心选择当前行最右边可放置的位置）
        p = available_positions & -available_positions

        # 将当前位置从可用位置中移除（准备处理下一个可能的位置）
        available_positions ^= p

        # 计算当前 p 对应的列号（通过位运算求出是第几位）
        col_index = p.bit_length() - 1
        queens.append(col_index)

        # 递归进入下一行，并更新三个冲突掩码
        backtrack(row + 1, col | p, (diag1 | p) << 1, (diag2 | p) >> 1)

        # 回溯：撤销选择
        queens.pop()

    # 初始时，第 0 行，所有冲突掩码都为 0
    backtrack(0, 0, 0, 0)
    return res
  