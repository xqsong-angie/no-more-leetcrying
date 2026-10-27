#20261021 AC

class Solution:
    def hammingWeight(self, n: int) -> int:
        res=""
        while n>0:
            res=str(n%2)+res
            n=n//2
        ans=0
        for r in res:
            if r=="1":
                ans+=1
        return ans