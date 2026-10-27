#20261022

#答案：https://algo.monster/liteproblems/1539
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Edge case: if arr[0] > k, all k missing numbers come before the array
        if arr[0] > k:
            return k

        # Binary search using the standard template
        # Feasible function: arr[mid] - mid - 1 >= k (at least k numbers missing before mid)
        left, right = 0, len(arr) - 1
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2

            # Calculate how many positive integers are missing before arr[mid]
            missing_count = arr[mid] - mid - 1

            if missing_count >= k:
                # Feasible: at least k missing numbers before this position
                first_true_index = mid
                right = mid - 1
            else:
                # Not feasible: need to search further right
                left = mid + 1

        # Calculate the kth missing number
        if first_true_index == -1:
            # All k missing numbers are after the array
            # Use the last element as anchor
            last_idx = len(arr) - 1
            missing_before_last = arr[last_idx] - last_idx - 1
            return arr[last_idx] + (k - missing_before_last)
        elif first_true_index == 0:
            # The kth missing number is before arr[0]
            return k
        else:
            # The kth missing number is between arr[first_true_index-1] and arr[first_true_index]
            prev_idx = first_true_index - 1
            missing_before_prev = arr[prev_idx] - prev_idx - 1
            return arr[prev_idx] + (k - missing_before_prev)
