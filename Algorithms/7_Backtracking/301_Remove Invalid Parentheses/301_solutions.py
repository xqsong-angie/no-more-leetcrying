#2061018

#答案：https://algo.monster/liteproblems/301 参数传递与隐式回溯（不可变对象）
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def dfs(index: int, left_to_remove: int, right_to_remove: int, 
                left_count: int, right_count: int, current_string: str) -> None:
            """
            Recursively explore all possible ways to remove invalid parentheses.
          
            Args:
                index: Current position in the original string
                left_to_remove: Number of '(' that still need to be removed
                right_to_remove: Number of ')' that still need to be removed
                left_count: Count of '(' in the current valid string being built
                right_count: Count of ')' in the current valid string being built
                current_string: The string being constructed
            """
            # Base case: reached end of string
            if index == string_length:
                # If all invalid parentheses have been removed, add to result
                if left_to_remove == 0 and right_to_remove == 0:
                    valid_results.add(current_string)
                return
          
            # Pruning conditions:
            # 1. Not enough characters left to remove required parentheses
            # 2. More closing than opening parentheses (invalid state)
            if string_length - index < left_to_remove + right_to_remove or left_count < right_count:
                return
          
            # Option 1: Remove current '(' if it needs to be removed
            if s[index] == '(' and left_to_remove > 0:
                dfs(index + 1, left_to_remove - 1, right_to_remove, 
                    left_count, right_count, current_string) #🔥传参回溯：我们每去下一层，就复印一份当前的进度给分身，分身怎么改都不影响主干道上的原件。因此从物理上看不需要“撤销”操作，当递归从深层返回时，上一层的变量天然就是它原本的样子。
          
            # Option 2: Remove current ')' if it needs to be removed
            elif s[index] == ')' and right_to_remove > 0:
                dfs(index + 1, left_to_remove, right_to_remove - 1, 
                    left_count, right_count, current_string)
          
            # Option 3: Keep current character (always explore this option)
            # Update counts if the character is a parenthesis
            new_left_count = left_count + (1 if s[index] == '(' else 0)
            new_right_count = right_count + (1 if s[index] == ')' else 0)
            dfs(index + 1, left_to_remove, right_to_remove, 
                new_left_count, new_right_count, current_string + s[index])
      
        # Step 1: Calculate how many left and right parentheses need to be removed
        left_to_remove = 0
        right_to_remove = 0
      
        for char in s:
            if char == '(':
                left_to_remove += 1
            elif char == ')':
                if left_to_remove > 0:
                    # This ')' can be paired with a previous '('
                    left_to_remove -= 1
                else:
                    # This ')' has no matching '(', needs to be removed
                    right_to_remove += 1
      
        # Initialize result set (using set to avoid duplicates)
        valid_results = set()
        string_length = len(s)
      
        # Start DFS exploration
        dfs(0, left_to_remove, right_to_remove, 0, 0, '')
      
        # Convert set to list for return
        return list(valid_results)
