#20261020

#答案
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        Determine if a frog can cross the river by jumping on stones.
        The frog starts at the first stone and each jump must be k-1, k, or k+1 units,
        where k is the distance of the previous jump.
      
        Args:
            stones: List of stone positions in ascending order
          
        Returns:
            True if the frog can reach the last stone, False otherwise
        """
        from functools import cache
      
        @cache
        def dfs(current_index: int, last_jump_distance: int) -> bool:
            """
            Depth-first search to check if frog can reach the last stone.
          
            Args:
                current_index: Current stone index the frog is on
                last_jump_distance: Distance of the previous jump
              
            Returns:
                True if frog can reach the last stone from current position
            """
            # Base case: reached the last stone
            if current_index == num_stones - 1:
                return True
          
            # Try all possible jump distances: k-1, k, k+1
            for next_jump_distance in range(last_jump_distance - 1, last_jump_distance + 2):
                # Calculate the target position after jumping
                target_position = stones[current_index] + next_jump_distance
              
                # Check if jump is valid (distance > 0) and target position has a stone
                if next_jump_distance > 0 and target_position in stone_position_to_index:
                    # Recursively check if we can reach the end from the new position
                    target_index = stone_position_to_index[target_position]
                    if dfs(target_index, next_jump_distance):
                        return True
          
            # No valid path found from current position
            return False
      
        # Initialize variables
        num_stones = len(stones)
        # Create a mapping from stone position to its index for O(1) lookup
        stone_position_to_index = {position: index for index, position in enumerate(stones)}
      
        # Start DFS from first stone (index 0) with initial jump distance 0
        return dfs(0, 0)
