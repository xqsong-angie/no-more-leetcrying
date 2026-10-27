#20261022

#答案
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # 1. 排序：宽度升序，宽度相同时高度降序
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # 2. 提取出高度数组，套用求 LIS 的二分查找模板
        heights = [env[1] for env in envelopes]
        
        tails = []#没看懂
        for h in heights:
            idx = bisect.bisect_left(tails, h)
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h
                
        return len(tails)
    
