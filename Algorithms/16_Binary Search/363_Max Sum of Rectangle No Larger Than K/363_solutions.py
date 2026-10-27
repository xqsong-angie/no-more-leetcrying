#20261022

#答案
from typing import List
from sortedcontainers import SortedList
import math

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Find the maximum sum of a rectangle in the matrix such that its sum is no larger than k.
      
        Args:
            matrix: 2D list of integers
            k: Target upper bound for rectangle sum
          
        Returns:
            Maximum sum of rectangle that doesn't exceed k
        """
        rows, cols = len(matrix), len(matrix[0])
        max_sum = -math.inf
      
        # Fix the top row of the rectangle
        for top_row in range(rows):
            # Initialize column sums for current top row
            column_sums = [0] * cols
          
            # Extend the rectangle by moving the bottom row down
            for bottom_row in range(top_row, rows):
                # Add current row values to column sums
                for col in range(cols):
                    column_sums[col] += matrix[bottom_row][col]
              
                # Now we have a 1D array problem: find max subarray sum <= k
                # Use prefix sum with sorted set to efficiently find the answer
                current_sum = 0
                # Store prefix sums in sorted order, initialize with 0
                prefix_sums = SortedList([0])
              
                for value in column_sums:
                    current_sum += value
                    # We need to find smallest prefix_sum such that:
                    # current_sum - prefix_sum <= k
                    # Which means: prefix_sum >= current_sum - k
                    target = current_sum - k
                    index = prefix_sums.bisect_left(target)#🔥没太看懂二分的部分，其他部分看懂了
                  
                    # If we found a valid prefix sum
                    if index < len(prefix_sums):
                        # Update max_sum with the rectangle sum
                        max_sum = max(max_sum, current_sum - prefix_sums[index])
                  
                    # Add current prefix sum for future iterations
                    prefix_sums.add(current_sum)
      
        return max_sum
