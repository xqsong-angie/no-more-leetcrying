#20261014
class Solution:
    def isInterleave(self,s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        
        # dp[i][j] 表示 s1 的前 i 个字符和 s2 的前 j 个字符能否组成 s3 的前 i+j 个字符
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = True
        
        # 初始化第一列（只用 s1 匹配）
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
            
        # 初始化第一行（只用 s2 匹配）
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            
        # 填表
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 状态转移
                from_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                from_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[i][j] = from_s1 or from_s2
                
        return dp[m][n]
        