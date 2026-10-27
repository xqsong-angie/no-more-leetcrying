#20261022 答案没太看懂

#答案
import bisect

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []
        for num in nums:
            # 二分查找（bisect_left）在 tails 中寻找第一个大于或等于 num 的位置
            idx = bisect.bisect_left(tails, num)
            
            # 如果 idx 等于 tails 的长度，说明 num 比所有元素都大，直接扩充序列
            if idx == len(tails):
                tails.append(num)
            else:
                # 否则，用 num 替换原位置的元素，贪心地让末尾元素尽可能小
                tails[idx] = num
                
        return len(tails) 