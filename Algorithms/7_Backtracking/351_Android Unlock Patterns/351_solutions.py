#20261018
class Solution:
    """
    @param m: an integer
    @param n: an integer
    @return: the total number of unlock patterns of the Android lock screen
    """
    def number_of_patterns(self, m: int, n: int) -> int:
        res=[]
        def backtracking(start,path):
            for i in range(start,10):
                if m<=len(path)<=n:
                    res.append(list(path))
                    path=[]
                elif len(path)>n:
                    return 
                direction=[(-1,-1),(-1,0),(1,1),(0,-1),(0,1),(-1,1),(1,0),(1,1)]
                for dx,dy in direction:
                    x=start//3+dx
                    y=start%3+dy
                    if 0<=x<=2 and 0<=y<=2:
                        new_start=x*3+y
                        path.append(new_start)
                        backtracking(new_start,path)
                        path.pop()
        backtracking(1,[])
        return len(res) #🔥memory limit exceeded, 我看出来android unlock pattern需要bfs
    
#答案：正确的做法是使用 DFS（深度优先搜索）+ 回溯
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # 记录两个点之间如果跨越了哪个中间点
        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2 #1，3之间跨越点2
        skip[1][7] = skip[7][1] = 4 #1,7之间跨越点4
        skip[1][9] = skip[9][1] = 5
        skip[3][7] = skip[7][3] = 5
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[2][8] = skip[8][2] = 5
        skip[4][6] = skip[6][4] = 5
        
        visited = [False] * 10
        
        def dfs(current, length):
            if length > n:
                return 0
            
            count = 1 if length >= m else 0
            visited[current] = True
            
            for next_node in range(1, 10):
                if not visited[next_node]:
                    intermediate = skip[current][next_node]
                    # 如果没有中间点，或者中间点已经被访问过，则可以走
                    if intermediate == 0 or visited[intermediate]:
                        count += dfs(next_node, length + 1)
                        
            visited[current] = False
            return count
        
        # 利用对称性优化：
        # 1 (角上的点，对应 1, 3, 7, 9)
        # 2 (边上的点，对应 2, 4, 6, 8)
        # 5 (中心点，对应 5)
        ans = 0
        ans += dfs(1, 1) * 4
        ans += dfs(2, 1) * 4
        ans += dfs(5, 1) * 1
        return ans