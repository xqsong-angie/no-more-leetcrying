#20261020

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        if not stations:
            if startFuel>=target:
                return 0
        else:
            m=len(stations)
            dp=[[0]*(m+1) for _ in range(2)]#离开idx加油站所剩最少能撑到终点的油量,可以选择取油和不取油两种
            dp[0][m]=target-stations[-1][0]#到达最后一个油桶的位置不取油，桶里需要剩
            dp[0][m]=target-stations[-1][0]-stations[-1][1]#到达最后一个油桶的位置取油，桶里需要剩

            for i in range(m-1,-1,-1):
                #不取油
                dp[0][i]=min(dp[1][i+1],dp[0][i+1])
                #取油
                dp[1][i]=min(dp[1][i+1],dp[0][i+1])-stations[i][1]#🔥写着写着就不知道是要实际有多少油还是需要多少油

#答案
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        n = len(stations)
        
        # dp[j] 表示加油 j 次能到达的最远距离
        # 一开始加油 0 次时，最远能走 startFuel 的距离
        dp = [0] * (n + 1)
        dp[0] = startFuel
        
        # 遍历每一个加油站
        for location, fuel in stations:
            # 必须倒序遍历，防止同一个加油站被重复使用多次（0/1 背包思想）
            for j in range(n - 1, -1, -1):
                # 如果当前加油 j 次能够到达该加油站，就可以尝试在这里加油
                if dp[j] >= location:
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)
        
        # 找到第一个能到达 target 的最小加油次数
        for j in range(n + 1):
            if dp[j] >= target:
                return j
                
        return -1
                    