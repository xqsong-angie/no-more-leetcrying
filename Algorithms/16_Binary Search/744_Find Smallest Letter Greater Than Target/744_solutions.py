#20251022

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        low=0
        high=len(letters)-1
        while low<=high:
            mid=(low+high)//2
            if letters[mid]==target:
                return letters[mid+1]
            elif letters[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return letters[0]
#题意理解错：Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
#不是target不在返回第一个，是target下一个不在返回第一个

#答案
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        low, high = 0, len(letters) - 1
        ans = letters[0]  # 🔥默认情况：如果没找到比 target 大的，返回第一个字符
        
        while low <= high:
            mid = (low + high) // 2
            if letters[mid] > target:
                ans = letters[mid]  # 记录当前满足条件的字符
                high = mid - 1      # 继续往左找，看看有没有更小的满足条件的字符
            else:
                low = mid + 1       # 字母太小或等于 target，往右找
                
        return ans