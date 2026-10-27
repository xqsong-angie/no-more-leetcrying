#20261022

class Solution:
    """
    @param sweetness: an integer array
    @param k: an integer
    @return:  return the maximum total sweetness of the piece
    """
    def maximize_sweetness(self, sweetness: List[int], k: int) -> int:
        # write your code here
        #k=0切一块，min_sweetness=sum(sweetness)
        #k=len(sweetness)-1,min_sweetness=min(sweetness)
        #0<=k<=len(sweetness)-1,min_sweetness=?
        low=0
        high=len(sweetness)-1
        #find the maximum min_sweetness
        max_min_sweetness=min(sweetness)
        while low<high:
            mid=(low+high)//2 #🔥搜索的变量应该是min_sweetness,不是k

#答案
class Solution:
    def maximize_sweetness(self, sweetness: List[int], k: int) -> int:
        num_pieces = k + 1
        low = min(sweetness)
        high = sum(sweetness) // num_pieces #🔥最大能达到的sweetness,这个要尽可能缩小范围
        
        ans = low
        while low <= high:
            mid = (low + high) // 2  # mid is our candidate for the minimum sweetness
            
            if self.can_split(sweetness, num_pieces, mid):
                ans = mid       # Feasible! Try to find an even larger minimum sweetness
                low = mid + 1
            else:
                high = mid - 1  # Too strict, reduce the target sweetness
                
        return ans

    def can_split(self, sweetness: List[int], num_pieces: int, target: int) -> bool:#🔥限制条件是num_pieces,这个不能变
        pieces = 0
        current_sum = 0
        for s in sweetness:
            current_sum += s
            if current_sum >= target:#巧克力必须取连续的几块给一个人，不能超，否则给下一个人
                pieces += 1
                current_sum = 0
        return pieces >= num_pieces
            
