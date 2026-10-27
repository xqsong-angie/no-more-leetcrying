#20261021 AC

class Solution:
    def findComplement(self, num: int) -> int:
        def dec_to_bin(num):
            res=""
            while num:
                if num%2==1:
                    res="1"+res
                else:
                    res="0"+res
                num=num//2
            return res
        def bin_to_dec(string):
            res=0
            rev=""
            for s in string:
                if s=="1":
                    rev+="0"
                else:
                    rev+="1"
            n=len(rev)
            for i in range(1,n+1):
                res+=int(rev[n-i])*2**(i-1)
            return res
        return bin_to_dec(dec_to_bin(num))