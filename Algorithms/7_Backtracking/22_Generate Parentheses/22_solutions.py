#20261008
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def isValid(path):
            stack=[]
            for p in path:
                if p=="(":
                    stack.append(p)
                else:
                    if not stack:
                        return False
                    else:
                        stack.pop()
            if stack:
                return False
            else:
                return True
        
        res=[]
        def backtracking(pt,n,path):
            for i in range(pt,2*n):
                pass
                #穷举是不是效率太低了

#答案
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(path: list, left: int, right: int):
            # 终止条件：当括号总数达到 2 * n 时放入结果
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            # 1. 优先尝试放左括号
            if left < n:
                path.append("(")
                backtrack(path, left + 1, right)
                path.pop()  # 回溯撤销操作

            # 2. 只有右括号少于左括号时，才能尝试放右括号
            if right < left:
                path.append(")")
                backtrack(path, left, right + 1)
                path.pop()  # 回溯撤销操作

        backtrack([], 0, 0)
        return res