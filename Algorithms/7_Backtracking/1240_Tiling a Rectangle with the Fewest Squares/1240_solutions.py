#20261009

#答案
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        def backtrack(row: int, col: int, num_squares: int) -> None:

            nonlocal min_squares
          
            # Move to next row if we've reached the end of current row
            if col == m:
                row += 1
                col = 0
          
            # If we've filled all rows, update the minimum answer
            if row == n:
                min_squares = num_squares
                return
          
            # If current cell is already filled, move to next cell
            if filled_cells[row] >> col & 1:
                backtrack(row, col + 1, num_squares)
            # Only continue if we can potentially get a better solution
            elif num_squares + 1 < min_squares:
                # Find maximum possible square size from current position
                max_rows = 0
                max_cols = 0
              
                # Count empty rows from current position
                for k in range(row, n):
                    if filled_cells[k] >> col & 1:
                        break
                    max_rows += 1
              
                # Count empty columns from current position
                for k in range(col, m):
                    if filled_cells[row] >> k & 1:
                        break
                    max_cols += 1
              
                # Maximum square size is limited by available rows and columns
                max_square_size = min(max_rows, max_cols)
              
                # Try all possible square sizes from 1 to max_square_size
                for square_size in range(1, max_square_size + 1):
                    # Mark cells as filled for current square
                    for k in range(square_size):
                        # Fill bottom row of the square
                        filled_cells[row + square_size - 1] |= 1 << (col + k)
                        # Fill rightmost column of the square
                        filled_cells[row + k] |= 1 << (col + square_size - 1)
                  
                    # Recursively try to fill remaining cells
                    backtrack(row, col + square_size, num_squares + 1)
              
                # Backtrack: unmark all cells that were filled
                for x in range(row, row + max_square_size):
                    for y in range(col, col + max_square_size):
                        filled_cells[x] ^= 1 << y
      
        # Initialize minimum squares to worst case (all 1x1 squares)
        min_squares = n * m
      
        # Track filled cells using bit manipulation (each row is a bitmask)
        filled_cells = [0] * n
      
        # Start backtracking from top-left corner
        backtrack(0, 0, 0)
      
        return min_squares
