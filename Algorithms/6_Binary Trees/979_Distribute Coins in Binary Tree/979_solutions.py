#20261008

#答案
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def distributeCoins(self, root: TreeNode | None) -> int:
        self.moves = 0

        def dfs(node):
            if not node:
                return 0

            # 后序计算左右子树的净盈余金币
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)

            # 左右子树与当前节点之间流动的金币总数就是步数
            self.moves += abs(left_balance) + abs(right_balance)

            # 返回以当前 node 为根的整棵子树的净盈余金币数
            return node.val + left_balance + right_balance - 1 #-1因为当前节点自己要留下一个金币

        dfs(root)
        return self.moves