#20261020
class Solution:
    def checkRecord(self, n: int) -> int:
        if n==1:
            return 3
        elif n==2:
            pass#应该也是dfs+memoization?但是n==2的case怎么递归

#答案
class Solution:
    def checkRecord(self, n: int) -> int:
        """
        Calculate the number of valid attendance records of length n.
        A valid record has:
        - At most 1 absence ('A')
        - No more than 2 consecutive late days ('L')
      
        Args:
            n: Length of the attendance record
          
        Returns:
            Number of valid attendance records modulo 10^9 + 7
        """
        from functools import cache
      
        MOD = 10**9 + 7
      
        @cache
        def dp(day: int, absence_count: int, consecutive_late: int) -> int:
            """
            Dynamic programming function to count valid attendance records.
          
            Args:
                day: Current day index (0-indexed)
                absence_count: Number of absences used so far (0 or 1)
                consecutive_late: Number of consecutive late days ending at current position
              
            Returns:
                Number of valid attendance records from this state
            """
            # Base case: reached the end of the record
            if day >= n:
                return 1
          
            result = 0
          
            # Option 1: Mark as Absent ('A') - only if no absence used yet
            if absence_count == 0:
                result += dp(day + 1, absence_count + 1, 0)
          
            # Option 2: Mark as Late ('L') - only if less than 2 consecutive lates
            if consecutive_late < 2:
                result += dp(day + 1, absence_count, consecutive_late + 1)
          
            # Option 3: Mark as Present ('P') - always allowed, resets consecutive late count
            result += dp(day + 1, absence_count, 0)
          
            return result % MOD
      
        # Calculate the answer starting from day 0 with no absences and no consecutive lates
        answer = dp(0, 0, 0)
      
        # Clear the cache to free memory
        dp.cache_clear()
      
        return answer


