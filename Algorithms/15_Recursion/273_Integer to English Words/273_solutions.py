#20261022

#答案
class Solution:
    def numberToWords(self, num: int) -> str:
        """
        Convert an integer to its English words representation.
      
        Args:
            num: Integer between 0 and 2^31 - 1
          
        Returns:
            String representation of the number in English words
        """
        # Special case for zero
        if num == 0:
            return 'Zero'
      
        # Words for numbers less than 20
        less_than_20 = [
            '',         # 0
            'One',      # 1
            'Two',      # 2
            'Three',    # 3
            'Four',     # 4
            'Five',     # 5
            'Six',      # 6
            'Seven',    # 7
            'Eight',    # 8
            'Nine',     # 9
            'Ten',      # 10
            'Eleven',   # 11
            'Twelve',   # 12
            'Thirteen', # 13
            'Fourteen', # 14
            'Fifteen',  # 15
            'Sixteen',  # 16
            'Seventeen',# 17
            'Eighteen', # 18
            'Nineteen', # 19
        ]
      
        # Words for tens places (10, 20, 30, ..., 90)
        tens_words = [
            '',         # 0
            'Ten',      # 10
            'Twenty',   # 20
            'Thirty',   # 30
            'Forty',    # 40
            'Fifty',    # 50
            'Sixty',    # 60
            'Seventy',  # 70
            'Eighty',   # 80
            'Ninety',   # 90
        ]
      
        # Scale words for thousands, millions, and billions
        scale_words = ['Billion', 'Million', 'Thousand', '']
      
        def convert_hundreds(num: int) -> str:
            """
            Convert a number less than 1000 to words.
          
            Args:
                num: Integer between 0 and 999
              
            Returns:
                String representation with trailing space
            """
            if num == 0:
                return ''
          
            # Handle numbers less than 20
            if num < 20:
                return less_than_20[num] + ' '
          
            # Handle numbers less than 100
            if num < 100:
                return tens_words[num // 10] + ' ' + convert_hundreds(num % 10)
          
            # Handle numbers from 100 to 999
            return less_than_20[num // 100] + ' Hundred ' + convert_hundreds(num % 100)
      
        # Build result by processing billions, millions, thousands, and ones
        result = []
        scale_divisor = 1_000_000_000  # Start with billions
        scale_index = 0
      
        while scale_divisor > 0:
            # Extract the current group (billions, millions, thousands, or ones)
            current_group = num // scale_divisor
          
            if current_group != 0:
                # Convert the group to words
                result.append(convert_hundreds(current_group))
                # Add the scale word (Billion, Million, Thousand, or empty)
                result.append(scale_words[scale_index])
                result.append(' ')
                # Remove the processed digits
                num %= scale_divisor
          
            # Move to the next scale
            scale_index += 1
            scale_divisor //= 1000
      
        # Join all parts and remove trailing whitespace
        return ''.join(result).strip()
