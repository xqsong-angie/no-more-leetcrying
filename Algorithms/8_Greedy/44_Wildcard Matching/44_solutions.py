#20261014
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i=j=0
        m=len(s)
        n=len(p)
        while i<m and j<n:
            if p[j]==s[i]:
                i+=1
                j+=1
            elif p[j]=="?":
                j+=1
                i+=1
            elif p[j]=="*":
                j+=1
                i=m
            else:
                return False
        if i==m and j==n:
            return True
        else:
            return False



#答案
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        m, n = len(s), len(p)
        starIdx = -1
        sTmpIdx = -1
        
        while i < m:
            # Case 1: 字符相等或者 p[j] 是 '?'
            if j < n and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            # Case 2: 遇到 '*'，记录位置，假设它匹配 0 个字符
            elif j < n and p[j] == '*':
                starIdx = j
                sTmpIdx = i
                j += 1
            # Case 3: 不匹配，但前面有 '*'，进行回溯让 '*' 多吞一个字符
            elif starIdx != -1:
                j = starIdx + 1#j回溯到上一个*的下一个位置
                sTmpIdx += 1
                i = sTmpIdx
            # Case 4: 不匹配且前面没有 '*'，匹配失败
            else:
                return False
                
        # 检查 p 剩下的部分是否全都是 '*'
        while j < n and p[j] == '*':
            j += 1
            
        return j == n