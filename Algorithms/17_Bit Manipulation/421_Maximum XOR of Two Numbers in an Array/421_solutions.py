#20261020
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        binary=[]
        for num in nums:
            res=""
            while num>=2:
                res=str(num%2)+res
                num=num//2
            res=res.zfill(32)
            binary.append(res) #https://www.w3schools.com/python/ref_string_zfill.asp
        
        for i in range(32):
            for b in binary:
                b[i]#到这里选最不一样的，要如何配对

#答案：https://algo.monster/liteproblems/421
from typing import List, Optional


class Trie:
    """Binary Trie for storing integers and finding maximum XOR."""
  
    __slots__ = ("children",)
  
    def __init__(self):
        # Each node has two children: 0 and 1 for binary representation
        self.children: List[Optional['Trie']] = [None, None]
  
    def insert(self, num: int) -> None:
        """
        Insert a number into the trie by its binary representation.
      
        Args:
            num: The integer to insert into the trie
        """
        current_node = self
      
        # Process bits from most significant to least significant (31 bits for int32)
        for bit_position in range(30, -1, -1):
            # Extract the bit at current position (0 or 1)
            bit_value = (num >> bit_position) & 1
          
            # Create new node if path doesn't exist
            if current_node.children[bit_value] is None:
                current_node.children[bit_value] = Trie()
          
            # Move to the next node
            current_node = current_node.children[bit_value]
  
    def search(self, num: int) -> int:
        """
        Find the maximum XOR value for the given number against all stored numbers.
      
        Args:
            num: The integer to find maximum XOR for
          
        Returns:
            The maximum XOR value possible with stored numbers
        """
        current_node = self
        max_xor = 0
      
        # Process bits from most significant to least significant
        for bit_position in range(30, -1, -1):
            # Extract the bit at current position
            bit_value = (num >> bit_position) & 1
          
            # Try to go opposite direction for maximum XOR
            # XOR is maximized when bits are different (0^1=1, 1^0=1)
            opposite_bit = bit_value ^ 1
          
            if current_node.children[opposite_bit] is not None:
                # If opposite bit path exists, take it and set this bit in result
                max_xor |= (1 << bit_position)
                current_node = current_node.children[opposite_bit]
            else:
                # Otherwise, follow the same bit path
                current_node = current_node.children[bit_value]
      
        return max_xor


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        Find the maximum XOR of two numbers in the array.
      
        Args:
            nums: List of non-negative integers
          
        Returns:
            Maximum XOR value of any two numbers in the array
        """
        # Build trie with all numbers
        trie = Trie()
        for num in nums:
            trie.insert(num)
      
        # Find maximum XOR for each number against all others
        return max(trie.search(num) for num in nums)


