#20261019
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        left_flag=0
        right_flag=0
        n=len(s) 
        dp=[0]*n #截至idx的longest substring
        for i in range(n):
            if s[i]=="(":
                left_flag+=1
            else:
                if left_flag:
                    dp[i]=dp[i-1]+2#🔥这里要分情况讨论
                    left_flag-=1
        return max(dp)
    
#答案
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        max_len = 0
        
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':#连续型
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':#包围型，里面是有效的
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
                
                max_len = max(max_len, dp[i])
                
        return max_len