#20261014

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp=[]
        n=len(triangle)
        for i in range(n):
            dp.append([0]*len(triangle[i]))
        
        #init
        sum=0
        for i in range(n):
            if i==0:
                dp[i][0]=triangle[i][0]
            else:
                dp[i][0]=sum+triangle[i][0]
            sum+=triangle[i][0]

        for i in range(1,n):
            for j in range(1,len(triangle[i])):
                dp[i][j]=min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]#🔥左右边界只有一个来源，需要特殊处理
        
        return min(dp[-1])
    
#答案
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        # 初始化 DP 表
        dp = [[0] * len(triangle[i]) for i in range(n)]
        
        dp[0][0] = triangle[0][0]
        
        for i in range(1, n):
            # 1. 左边界：只能由上一行的第一个累加下来
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            
            # 2. 中间元素：由上一行的左上方或正上方转移而来
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
                
            # 3. 右边界：只能由上一行的最后一个累加下来
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
            
        return min(dp[-1])