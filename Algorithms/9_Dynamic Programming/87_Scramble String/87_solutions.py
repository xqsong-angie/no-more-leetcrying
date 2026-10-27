#20261019

#答案：https://algo.monster/liteproblems/87
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:#🔥与最值类dp不同，这个更像是recursion+memoization
        """
        Determines if s2 is a scrambled string of s1.
        A scrambled string is formed by recursively dividing the string into two non-empty substrings
        and potentially swapping them.
      
        Args:
            s1: The original string
            s2: The string to check if it's a scrambled version of s1
          
        Returns:
            True if s2 is a scrambled string of s1, False otherwise
        """
        from functools import cache
      
        @cache
        def is_scramble_substring(start_s1: int, start_s2: int, length: int) -> bool:
            """
            Recursively checks if a substring of s2 is a scrambled version of a substring of s1.
          
            Args:
                start_s1: Starting index in s1
                start_s2: Starting index in s2
                length: Length of the substring to check
              
            Returns:
                True if the substrings match as scrambled strings, False otherwise
            """
            # Base case: single character comparison
            if length == 1:
                return s1[start_s1] == s2[start_s2]
          
            # 🔥Try all possible split points
            for split_point in range(1, length):
                left_length = split_point #左半长度
                right_length = length - split_point #右半长度
              
                # Case 1: No swap occurred at this level
                # Check if left parts match and right parts match
                if (is_scramble_substring(start_s1, start_s2, left_length) and 
                    is_scramble_substring(start_s1 + left_length, start_s2 + left_length, right_length)):
                    return True
              
                # Case 2: Swap occurred at this level
                # Check if left part of s1 matches right part of s2 and vice versa
                if (is_scramble_substring(start_s1 + left_length, start_s2, right_length) and 
                    is_scramble_substring(start_s1, start_s2 + right_length, left_length)):
                    return True
          
            # No valid split found
            return False
      
        # Start the recursive check from the beginning of both strings
        return is_scramble_substring(0, 0, len(s1))

