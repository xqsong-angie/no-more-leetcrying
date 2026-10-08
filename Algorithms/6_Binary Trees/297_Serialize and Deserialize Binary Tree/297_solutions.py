#20261002
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        else:
            res=[]
            queue=deque([root])
            while queue:
                top=queue.popleft()
                if top!=None:
                    res.append(str(top.val))
                    if top.left:
                        queue.append(top.left)
                    else:
                        queue.append(None)
                    if top.right:
                        queue.append(top.right)
                    else:
                        queue.append(None)
            
                else:
                    res.append("None")

        return " ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        else:
            data_splited=data.split()#🔥这是前序的解码，序列化和反序列化必须用同一套遍历逻辑
            def helper(data_splited,pt):
                if pt<len(data_splited)-2:
                    root=TreeNode(data_splited[pt])
                    helper(root.left,pt+1)
                    helper(root.right,pt+2)
                else:
                    return
            helper(data_splited,0)
            return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

#答案
from collections import deque

class Codec:
    def serialize(self, root):
        if not root: return ""
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("None")
        return " ".join(res)

    def deserialize(self, data):
        if not data: return None
        
        data_splited = data.split()
        
        # 1. 先把根节点建出来，并放入队列 (注意把字符串转回 int)
        root = TreeNode(int(data_splited[0]))
        queue = deque([root])
        
        # 2. i 用来遍历 data_splited 数组，从下标 1 (即根节点的左子节点) 开始
        i = 1 
        
        while queue:
            # 每次从队列弹出一个已经建好的父亲节点
            node = queue.popleft()
            
            # 处理左子节点
            if data_splited[i] != "None":
                node.left = TreeNode(int(data_splited[i]))
                queue.append(node.left)
            i += 1  # 无论是不是 None，数组指针都要往后走一步
            
            # 处理右子节点
            if data_splited[i] != "None":
                node.right = TreeNode(int(data_splited[i]))
                queue.append(node.right)
            i += 1  # 无论是不是 None，数组指针都要往后走一步
            
        return root