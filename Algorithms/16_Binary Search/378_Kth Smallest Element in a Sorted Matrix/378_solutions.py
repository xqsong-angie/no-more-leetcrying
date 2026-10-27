#20261023

#答案：在值上二分搜索
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Find the kth smallest element in a sorted matrix using binary search.

        Feasible condition: count of elements <= mid is >= k.
        We find the first value where this is true.

        Args:
            matrix: n x n matrix where each row and column is sorted in ascending order
            k: the kth position to find (1-indexed)

        Returns:
            The kth smallest element in the matrix
        """
        n = len(matrix)

        def count_less_equal(target: int) -> int:
            """Count elements <= target using staircase search from bottom-left."""
            count = 0
            row, col = n - 1, 0

            while row >= 0 and col < n:#限制条件
                if matrix[row][col] <= target:
                    count += row + 1 #沿着column计数
                    col += 1
                else:
                    row -= 1

            return count

        def feasible(mid: int) -> bool:
            """Check if there are at least k elements <= mid."""
            return count_less_equal(mid) >= k

        # Binary search on value range
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return first_true_index
