#20261008
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        else:
            queue=deque([root])
            while queue:
                length=len(queue)
                while length:
                    cur=None #🔥cur,cnt,prev不能放在length内部，这样同一层每一个节点都会丢掉邻居节点的信息
                    cnt=0
                    prev=None
                    if length==1:
                        cur=queue.popleft()
                        cur.next=None
                    elif cnt==0:
                        prev=None
                        cur=queue.popleft()
                    else:
                        prev=cur
                        cur=queue.popleft()
                        prev.next=cur
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                    cnt+=1
                    length-=1
            return root

#答案
from collections import deque
class Solution:

    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        queue = deque([root])

        while queue:
            length = len(queue)
            prev = None  # 在每一层开始前初始化前驱节点

            for _ in range(length):
                cur = queue.popleft()

                # 如果前面有节点，把上一个节点的 next 指向当前节点
                if prev:
                    prev.next = cur
                prev = cur  # 更新 prev 为当前节点

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            # 最后一层的最后一个节点的 next 默认为 None，不需要额外处理

        return root