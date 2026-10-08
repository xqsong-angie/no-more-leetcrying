#20261008

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        queue=deque([root])
        layer=0
        while queue:
            length=len(queue)
            if 2**layer==length:
                while length:
                    cur=queue.popleft()
                    if cur.left:
                        queue.append(cur.left)
                        if cur.right:#🔥中间空一块的如果是右节点没法处理
                            queue.append(cur.right)
                    else:
                        if cur.right:
                            return False
                    length-=1
            else:
                while length:
                    cur=queue.popleft()
                    if cur.left or cur.right:
                        return False
                    length-=1
            layer+=1
        return True
                
#答案
from collections import deque


class Solution:

    def isCompleteTree(self, root: TreeNode | None) -> bool:
        queue = deque([root])
        seen_null = False  # 标记是否已经遇到过空节点

        while queue:
            node = queue.popleft()

            if not node:
                seen_null = True  # 记录遇到了空节点
            else:
                if seen_null:
                    # 之前已经遇到过空节点，现在又出现了非空节点 -> 说明中间空了一块
                    return False

                # 🔥无论子节点是否为空，都直接按从左到右入队
                queue.append(node.left)
                queue.append(node.right)

        return True