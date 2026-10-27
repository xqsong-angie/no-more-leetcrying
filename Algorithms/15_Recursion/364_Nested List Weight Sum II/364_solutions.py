#20261023

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class Solution:
    """
    @param nestedList: a list of NestedInteger
    @return: the sum
    """
    def depthSumInverse(self, nestedList):
        self.total=0
        def rec(nestedList,depth):
            for ele in nestedList:
                if ele.isInteger():
                    self.total=depth*ele.getInteger() #🔥新值会覆盖旧值
                else:
                    rec(ele.getList(),depth+1)
        rec(nestedList,1)
        return self.total

#没有读完题，这次是逆深度权重

#答案
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        """
        Calculate the inverse depth sum of a nested list.
        Each integer is multiplied by its inverse depth weight.

        Args:
            nestedList: A list of NestedInteger objects

        Returns:
            The sum where each integer is weighted by (max_depth - current_depth + 1)
        """

        def traverse_nested_list(nested_integer, current_depth):
            """
            Recursively traverse the nested structure to calculate sums and find max depth.

            Args:
                nested_integer: Current NestedInteger object to process
                current_depth: Current depth level (starting from 1)
            """
            nonlocal max_depth, total_sum, weighted_sum_by_depth

            # Track the maximum depth of any integer (empty lists do not count)
            max_depth = max(max_depth, current_depth) if nested_integer.isInteger() else max_depth

            if nested_integer.isInteger():
                # If it's a single integer, add it to our sums
                integer_value = nested_integer.getInteger()
                total_sum += integer_value  # Sum of all integers
                weighted_sum_by_depth += integer_value * current_depth  # Sum weighted by depth
            else:
                # If it's a list, recursively process each element at the next depth level
                for nested_element in nested_integer.getList():
                    traverse_nested_list(nested_element, current_depth + 1)

        # Initialize tracking variables
        max_depth = 0  # Maximum depth found in the nested structure
        total_sum = 0  # Sum of all integers regardless of depth
        weighted_sum_by_depth = 0  # Sum of integers weighted by their depth

        # Process each top-level element in the nested list
        for nested_element in nestedList:
            traverse_nested_list(nested_element, 1)

        # Calculate inverse depth sum using the formula:
        # For each integer v at depth d: contribution = v * (max_depth - d + 1)
        # Total = Σ(v * (max_depth - d + 1)) = (max_depth + 1) * Σv - Σ(v * d)
        return (max_depth + 1) * total_sum - weighted_sum_by_depth

