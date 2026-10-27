#20261014
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        cnt=Counter(tasks)
        res=0
        time_passed={}
        while any(cnt.values())>0:
            mytuple=list(cnt.items()).sort(key=lambda x: (-x[1],x[0]))#🔥：list.sort没有返回值
            for k,v in mytuple:
                if k not in set(time_passed.keys()):
                    cnt[k]-=1
                elif time_passed[k]>=2:
                    if k in set(time_passed.keys()):
                        cnt[k]-=1

                for _,v in time_passed.items():
                    v+=1
                    time_passed[k]=0
                res+=1
        return res
    
#答案
from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        
        # Count how many tasks have this maximum frequency
        max_count = sum(1 for freq in counts.values() if freq == max_freq)
        
        # The minimum intervals needed based on the most frequent task
        part_count = max_freq - 1 #每个有max_freq个的task需要part_count个空位
        part_length = n - (max_count - 1)#每个空位需要max_count - 1个去填补，如果不够就会有idle
        empty_slots = part_count * part_length
        
        # Available tasks to fill the empty slots
        available_tasks = len(tasks) - (max_freq * max_count)#剩余未用任务
        idles = max(0, empty_slots - available_tasks)
        
        return len(tasks) + idles
    
