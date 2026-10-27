#20261009

class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        def isValid(first_num,sec_num,rest_str):
            prev_sum=int(first_num)+int(sec_num)
            if prev_sum>0 and rest_str[0]==0:
                return False
            else:
                if rest_str.startswith(str(prev_sum)) and isValid(sec_num,str(prev_sum),rest_str[len(str(prev_sum)):]):
                    return True
                else:
                    return False
        n=len(num)
        def backtracking():
            for first_num_end in range(1,n-2):
                for sec_num_end in range(first_num_end+1,n-1):
                    first_num=num[:first_num_end+1]
                    sec_num=num[first_num_end+1:sec_num_end+1]
                    if isValid(first_num,sec_num,num[sec_num_end+1:]):
                        return 
                    else:
                        backtracking(first_num)#如何返回结果以及回溯？

#答案
class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        n = len(num)
        ans = []

        def backtrack(index: int) -> bool:
            # Base condition: 遍历到了字符串末尾，且至少拆分出了 3 个数字
            if index == n and len(ans) >= 3:
                return True
            
            # 尝试从 index 开始切分下一个数字
            for i in range(index, n):
                # 1. 剪枝：处理前导零（如果当前数以 '0' 开头，它只能是单独的 0）
                if num[index] == '0' and i > index:
                    break
                
                # 2. 截取数字并检查 32 位有符号整数溢出限制（题目要求 <= 2^31 - 1）
                curr = int(num[index : i + 1])
                if curr > 2**31 - 1:
                    break
                
                # 3. 检查斐波那契属性：如果已有 >= 2 个数，当前数必须等于前两数之和
                if len(ans) >= 2:
                    expected_sum = ans[-1] + ans[-2]
                    if curr < expected_sum:
                        continue  # 当前数还不够大，继续增加长度
                    elif curr > expected_sum:
                        break    # 当前数已经超过预期值，再往后切只会更大，直接剪枝
                
                # 4. 做选择（入栈）
                ans.append(curr)
                
                # 递归探索下一个位置
                if backtrack(i + 1):
                    return True  # 找到了合法解，直接逐层向上返回 True，保留 ans
                
                # 5. 撤销选择（回溯/出栈）
                ans.pop()
            
            return False

        backtrack(0)
        return ans