#20261006
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead. in-place怎么保存之前的结果呢
        """
        if not root:
            return None#🔥函数不返回任何结果
        else:
            if not root.left and not root.right:
                return root #🔥函数不返回任何结果
            else:
                stack=[root]
                while stack:
                    top=stack.pop()
                    if root.right:
                        stack.append(root.right)
                    if root.left:
                        stack.append(root.left)

#答案：
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        if not root:
            return
        
        stack = [root]
        prev = None  # 用来记录上一个遍历到的节点
        
        while stack:
            curr = stack.pop()
            
            # 如果存在上一个节点，就把当前节点接在上一个节点的 right 上
            if prev:
                prev.left = None   # 题目要求 left 清空
                prev.right = curr
            
            # 先压右，再压左（出栈时就是先左后右）
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            
            # 更新 prev 为当前节点
            prev = curr