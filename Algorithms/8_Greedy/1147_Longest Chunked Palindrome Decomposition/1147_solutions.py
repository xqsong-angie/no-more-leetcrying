#20261014

#答案：段式回文，且要切尽可能多的段
class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        if not text:
            return 0
        
        # 尝试从两头往中间匹配
        for i in range(1, n // 2 + 1):
            # 如果前缀和后缀相等
            if text[:i] == text[n - i:]:#贪心：一相等就递归处理中间，保证两头最短
                # 递归处理中间剩余的部分，并加上两头的 2 段
                return 2 + self.longestDecomposition(text[i:n - i])
                
        # 如果两头怎么都凑不出相等的块，说明整个字符串只能作为完整的一块
        return 1