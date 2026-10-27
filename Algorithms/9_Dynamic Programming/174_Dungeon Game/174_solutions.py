#20261014

#答案
class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # 创建 (m+1) x (n+1) 的 DP 表，多出来的一行一列初始化为正无穷 (inf)
        # 这样当我们在最后一行或最后一列时，访问右边或下边的格子就不会越界
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # 核心边界初始化：
        # 设置终点右侧和下方的虚拟边界为 1，多出来的1保证血条不降到0
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1
        
        # 从右下角（终点附近）开始，逆向遍历到左上角（起点）
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 下一步所需的最小血量：取向右走或向下走的最小值
                min_next_hp = min(dp[i + 1][j], dp[i][j + 1])
                
                # 减去当前格子提供的血量，并保证血量至少为 1
                dp[i][j] = max(1, min_next_hp - dungeon[i][j])
                
        # 返回起点所需的最小初始血量
        return dp[0][0]