#20261021

class Solution:
    def reverseBits(self, n: int) -> int:
        res=""
        while n>0:
            res=str(n%2)+res
            n=n//2
        #reverse string https://stackoverflow.com/questions/931092/how-do-i-reverse-a-string-in-python
        
        res_rev=res[::-1]
        ans=0
        pow=0
        for i in range(len(res_rev)-1,-1,-1):
            ans+=int(res_rev[i])*2**pow
            pow+=1
        return ans#🔥忘记补全前导0
    
#答案
class Solution:

  def reverseBits(self, n: int) -> int:
    # 1. 转成二进制，去掉前缀 '0b'，并用 zfill(32) 补齐 32 位
    bin_str = bin(n)[2:].zfill(32)
    # 2. 字符串反转
    rev_str = bin_str[::-1]
    # 3. 将二进制字符串转回十进制整数
    return int(rev_str, 2)