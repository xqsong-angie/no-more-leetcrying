#20261007

#答案
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        self.max_diameter = 0

        def depth(node: TreeNode | None) -> int:
            if not node:
                return 0
            
            # 递归计算左右子树的深度
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # 以当前节点为顶点的最长路径（边数）= 左深度 + 右深度
            current_diameter = left_depth + right_depth
            
            # 更新全局最大直径
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # 返回当前节点自身的最大深度（给上一层父节点使用）
            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.max_diameter