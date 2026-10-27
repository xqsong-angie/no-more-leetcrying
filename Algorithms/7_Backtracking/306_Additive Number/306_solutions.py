#20261009

#答案：https://algo.monster/liteproblems/306
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def validate_sequence(first_num: int, second_num: int, remaining_str: str) -> bool:
            if not remaining_str:
                return True
          
            expected_sum = first_num + second_num
            if expected_sum > 0 and remaining_str[0] == '0':
                return False

            for next_num_length in range(1, len(remaining_str) + 1):
                potential_next_num = int(remaining_str[:next_num_length])
              
                if potential_next_num == expected_sum:
                    if validate_sequence(second_num, expected_sum, remaining_str[next_num_length:]):
                        return True
          
            return False
      
        string_length = len(num)
      
        for first_num_end in range(1, string_length - 1):
            if first_num_end > 1 and num[0] == '0':
                break
              
            for second_num_end in range(first_num_end + 1, string_length):
                if second_num_end - first_num_end > 1 and num[first_num_end] == '0':
                    continue

                first_number = int(num[:first_num_end])
                second_number = int(num[first_num_end:second_num_end])
              
                if validate_sequence(first_number, second_number, num[second_num_end:]):
                    return True
      
        return False
