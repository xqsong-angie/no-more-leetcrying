#20250724
class Solution:
    def numDecodings(self,s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0

        f = [0] * (n + 1)
        f[0] = 1  # 空字符串的解法数是 1（用于 DP 初值）
        f[1] = 1  # 第一个字符有效，只有 1 种解法

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digit = int(s[i - 2:i])

            # 单个数字有效（1-9）
            if 1 <= one_digit <= 9:
                f[i] += f[i - 1]

            # 两位数有效（10-26）
            if 10 <= two_digit <= 26:
                f[i] += f[i - 2]

        return f[n]

#20261020 看了一遍