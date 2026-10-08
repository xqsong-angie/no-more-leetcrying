#20261008 AC

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        queue=deque([root])
        mysum=0
        while queue:
            mysum=0
            length=len(queue)
            while length:
                cur=queue.popleft()
                mysum+=cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                length-=1
        return mysum
