#20261008
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        hr=[0,1,2,4,8]
        mi=[0,1,2,4,8,16,32]

        self.res=[]
        self.h=0
        self.m=0 #hr和mi是否要分开处理
        def backtracking(turnedOn):
            for i in hr:
                self.h+=hr
                
                backtracking()
        

#答案
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        # 代表 10 个 LED 灯对应的数值
        # 前 4 个是小时 (8, 4, 2, 1)，后 6 个是分钟 (32, 16, 8, 4, 2, 1)
        leds = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        res = []

        def backtrack(idx: int, count: int, h: int, m: int):
            # 剪枝：如果小时或分钟超出合法范围，直接返回
            if h >= 12 or m >= 60:
                return
            
            # 终止条件：亮灯数量达到要求
            if count == turnedOn:
                res.append(f"{h}:{m:02d}")
                return

            # 遍历剩余的灯
            for i in range(idx, 10):
                if i < 4:
                    # 前 4 个灯属于小时
                    backtrack(i + 1, count + 1, h + leds[i], m)
                else:
                    # 后 6 个灯属于分钟
                    backtrack(i + 1, count + 1, h, m + leds[i])

        backtrack(0, 0, 0, 0)
        return res