#20261002
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.original=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.original.append(root.val)
            inorder(root.right)
        inorder(root)
        self.original.sort()
        def inorder2(root,i):
            if not root:
                return 
            inorder2(root.left,i) #i 要变成全局,不能使用参数传递，回退到该层的时候无法记住最新的i
            root.val=self.original[i]
            i+=1
            inorder2(root.right,i)
        inorder2(root,0)
        return root
    
#答案
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.original=[]
        self.i=0
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.original.append(root.val)
            inorder(root.right)
        inorder(root)
        self.original.sort()
        def inorder2(root):
            if not root:
                return 
            inorder2(root.left)
            root.val=self.original[self.i]
            self.i+=1
            inorder2(root.right)
        inorder2(root)
        return root