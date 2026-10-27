#20261021

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        res=""
        while head:
            res=str(head.val)+res#🔥字符串拼接方向反了
            head=head.next
        pow=0
        ans=0
        for i in range(len(res)-1,-1,-1):
            ans+=int(res[i])*2**pow
            pow+=1
        return ans
    
#答案
class Solution:

  def getDecimalValue(self, head: ListNode | None) -> int:
    ans = 0
    while head:
      # 将当前结果左移一位（相当于乘以 2），再加上当前节点的值
      ans = (ans << 1) | head.val
      head = head.next
    return ans