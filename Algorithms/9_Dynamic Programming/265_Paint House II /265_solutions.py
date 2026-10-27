#20261020
from typing import (
    List,
)

class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def min_cost_i_i(self, costs: List[List[int]]) -> int:
        # write your code here
        n=len(costs)#houses
        k=len(costs[0])#colors
        dp=[[0]*k for _ in range(n)]
        #只有一个颜色时
        for i in range(n):
            dp[i][0]#🔥无法初始化，因为必须要至少两个颜色

#答案
from typing import List

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if not costs or not costs[0]:
            return 0
            
        k = len(costs[0])
        if n == 1:
            return min(costs[0])
        elif k == 1:
            return 0
            
        # dp_prev 表示上一栋房子涂各颜色时的最小累计花费
        dp_prev = costs[0][:]

        for house_idx in range(1, n):
            # 1. 在更新当前行之前，先找出上一行(dp_prev)的 min1, min1_idx, min2
            min1_val, min1_idx, min2_val = float('inf'), -1, float('inf')
            for idx, val in enumerate(dp_prev):
                if val < min1_val:
                    min2_val = min1_val
                    min1_val = val
                    min1_idx = idx
                elif val < min2_val:
                    min2_val = val

            dp_curr = [0] * k
            # 2. O(1) 转移，彻底消灭内层的 min 遍历
            for curr_color in range(k):
                # 如果当前颜色撞上了上一行的最小值索引，就退而求其次选次小值
                prev_best = min2_val if curr_color == min1_idx else min1_val
                dp_curr[curr_color] = costs[house_idx][curr_color] + prev_best

            dp_prev = dp_curr

        return min(dp_prev)