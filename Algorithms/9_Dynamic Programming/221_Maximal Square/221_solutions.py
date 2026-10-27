#2026118 有bug
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0]*n for _ in range(m)]#以当前块为右下角的最大边长
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    dp[i][j]=1

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=="1" and matrix[i-1][j]=="1" and matrix[i][j-1]=="1":
                    dp[i][j]=dp[i-1][j-1]+1 #🔥缺少限定条件导致结果过大
        res=0
        for i in range(m):
            for j in range(n):
                res=max(res,dp[i][j])
        return res**2
    
#答案
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    # 第一行和第一列的边界条件，最大边长只能是 1
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # 核心补充条件：取左、上、左上(否则左上角可能是空的）三个方向的最小值 + 1
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    res = max(res, dp[i][j])
                    
        return res ** 2