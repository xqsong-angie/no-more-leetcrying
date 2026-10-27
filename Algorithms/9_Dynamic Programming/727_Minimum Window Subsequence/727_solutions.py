#20261019

#答案
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        len_s1, len_s2 = len(s1), len(s2)

        # dp[i][j] stores the starting index (1-based) in s1 where
        # the subsequence s2[0:j] ends at position i in s1
        # 0 means no valid subsequence found
        dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

        # Fill the dp table
        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    # Characters match
                    if j == 1:
                        # First character of s2, start index is current position
                        dp[i][j] = i
                    else:
                        # Continue from previous subsequence
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Characters don't match, inherit from previous position in s1
                    dp[i][j] = dp[i - 1][j]

        # Find the minimum window
        start_index = 0
        min_length = len_s1 + 1

        for i in range(1, len_s1 + 1):
            # Check if s1[i-1] matches the last character of s2
            # and we have a valid subsequence ending at position i
            if s1[i - 1] == s2[len_s2 - 1] and dp[i][len_s2] != 0:
                # Calculate window start (0-based) and length
                window_start = dp[i][len_s2] - 1
                window_length = i - window_start

                # Update minimum window if current one is smaller
                if window_length < min_length:
                    min_length = window_length
                    start_index = window_start

        # Return the minimum window substring or empty string if not found
        return "" if min_length > len_s1 else s1[start_index : start_index + min_length]
