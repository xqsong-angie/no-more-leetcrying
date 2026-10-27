#20261016

#答案：https://algo.monster/liteproblems/464
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """
        Determines if the first player can force a win in a game where players
        take turns choosing integers from 1 to maxChoosableInteger (without replacement)
        and the first to reach or exceed desiredTotal wins.
      
        Args:
            maxChoosableInteger: The maximum integer that can be chosen (1 to maxChoosableInteger)
            desiredTotal: The target sum to reach or exceed to win
          
        Returns:
            True if the first player can guarantee a win, False otherwise
        """
        from functools import cache
      
        @cache
        def can_win_from_state(used_numbers_mask: int, current_sum: int) -> bool:
            """
            Recursively determines if the current player can win from the given state.
          
            Args:
                used_numbers_mask: Bitmask representing which numbers have been used
                                   (bit i represents whether number i has been used)
                current_sum: The current running total
              
            Returns:
                True if the current player can force a win from this state
            """
            # Try each possible number from 1 to maxChoosableInteger
            for number in range(1, maxChoosableInteger + 1):
                # Check if this number hasn't been used yet
                # (bit at position 'number' should be 0)
                if (used_numbers_mask >> number) & 1 == 0:
                    # Calculate new sum after choosing this number
                    new_sum = current_sum + number
                  
                    # Current player wins if either:
                    # 1. This move reaches or exceeds the desired total
                    # 2. The opponent cannot win from the resulting state
                    if new_sum >= desiredTotal:
                        return True
                  
                    # Mark this number as used and check opponent's position
                    new_mask = used_numbers_mask | (1 << number)
                    if not can_win_from_state(new_mask, new_sum):
                        return True
          
            # If no winning move exists, current player loses
            return False
      
        # Early termination: if the sum of all available numbers is less than
        # the desired total, nobody can win (first player loses)
        total_available_sum = (1 + maxChoosableInteger) * maxChoosableInteger // 2
        if total_available_sum < desiredTotal:
            return False
      
        # Start the game with no numbers used and sum of 0
        return can_win_from_state(0, 0)
