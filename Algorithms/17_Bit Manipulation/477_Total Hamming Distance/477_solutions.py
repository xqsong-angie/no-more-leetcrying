#20261020

#答案
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        Calculate the total Hamming distance between all pairs of integers in the array.
      
        The Hamming distance between two integers is the number of positions at which
        the corresponding bits are different.
      
        Args:
            nums: List of integers
          
        Returns:
            Total Hamming distance between all pairs
        """
        total_distance = 0
        array_length = len(nums)
      
        # Check each bit position (0 to 31 for 32-bit integers)
        for bit_position in range(32): #所有元素转成定长二进制数
            # Count how many numbers have a 1 at this bit position
            ones_count = sum((num >> bit_position) & 1 for num in nums)
          
            # Count how many numbers have a 0 at this bit position
            zeros_count = array_length - ones_count
          
            # For this bit position, the contribution to total Hamming distance
            # is the number of (1, 0) pairs, which equals ones_count * zeros_count
            total_distance += ones_count * zeros_count
      
        return total_distance
