#20261022

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start=end=-1
        low=0
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if mid==target:#🔥混淆了索引和值
                start=end=mid
                while nums[start]==target:#🔥如果数组中全是target容易退化为O(n),失去了二分查找的意义
                    start-=1
                start+=1
                while nums[end]==target:
                    end+=1
                end-=1
                break
            elif mid<target:
                low=mid+1
            else:
                high=mid-1
        return [start,end]
    
#答案
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findFirst(nums, target):
            low, high = 0, len(nums) - 1
            first = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1  # 🔥核心：找到了先记录，然后继续往左找，看看还有没有更靠前的
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        def findLast(nums, target):
            low, high = 0, len(nums) - 1
            last = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last = mid
                    low = mid + 1   # 🔥核心：找到了先记录，然后继续往右找，看看还有没有更靠后的
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last

        return [findFirst(nums, target), findLast(nums, target)]
    