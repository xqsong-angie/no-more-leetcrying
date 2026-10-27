#20261027

from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        count=0
        intervals.sort(key=lambda x: (x.start,x.end))
        for i in range(len(intervals)):
            if i==0:
                count+=1
            else:
                if intervals[i].start<=intervals[i].end:#🔥intervals[i-1]
                    count+=1
        return count


#答案
from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # 1. 按照会议开始时间排序
        intervals.sort(key=lambda x: x.start)
        
        # 2. 使用最小堆记录会议室的结束时间
        rooms = []
        heapq.heappush(rooms, intervals[0].end)
        
        for i in range(1, len(intervals)):
            # 如果当前会议开始时间大于等于最早结束的会议室结束时间，复用该会议室
            if intervals[i].start >= rooms[0]:
                heapq.heappop(rooms)
            
            # 将当前会议的结束时间放入堆中
            heapq.heappush(rooms, intervals[i].end)
            
        # 堆中剩余的元素个数就是最少需要的会议室数量
        return len(rooms)
