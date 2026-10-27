#20261021

#这题范围很大，感觉有不遍历的方法，但是想不到

#答案：https://algo.monster/liteproblems/201
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Find the bitwise AND of all numbers in the range [left, right] inclusive.
      
        The key insight is that the result will be the common prefix of left and right
        in their binary representations. We achieve this by repeatedly clearing the 
        rightmost set bit of 'right' until right becomes less than or equal to left.
      
        Args:
            left: The starting number of the range (inclusive)
            right: The ending number of the range (inclusive)
      
        Returns:
            The bitwise AND of all numbers in the range [left, right]
        """
        # Keep removing the rightmost set bit from 'right'
        # until 'right' becomes less than or equal to 'left'
        while left < right:
            # Clear the rightmost set bit in 'right'
            # This operation: right & (right - 1) removes the last set bit
            # Example: 12 (1100) & 11 (1011) = 8 (1000)
            right &= right - 1
      
        # At this point, 'right' contains the common prefix bits
        # that remain set in all numbers from left to right
        return right
