#20261020

#答案
from typing import List
from bisect import bisect_left

class Solution:#隐式dp+二分查找优化
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort envelopes by width ascending, and if widths are equal, by height descending
        # This ensures we can't use two envelopes with the same width in our sequence
        envelopes.sort(key=lambda envelope: (envelope[0], -envelope[1]))#宽度升序，高度降序
      
        # Initialize LIS (Longest Increasing Subsequence) array with the first envelope's height
        # This array maintains the smallest tail value for each possible subsequence length
        lis_heights = [envelopes[0][1]]#最窄的那个信封的高度
      
        # Process remaining envelopes
        for width, height in envelopes[1:]:#后面的信封
            if height > lis_heights[-1]:
                # If current height is larger than the largest height in LIS,
                # we can extend the sequence
                lis_heights.append(height)
            else:
                # Find the leftmost position where we can replace an existing height
                # with the current height to maintain the LIS property
                insertion_index = bisect_left(lis_heights, height)
                lis_heights[insertion_index] = height#这里还是没看懂
      
        # The length of the LIS array represents the maximum number of envelopes
        # that can be nested (Russian doll style)
        return len(lis_heights)
