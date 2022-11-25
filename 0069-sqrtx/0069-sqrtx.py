class Solution:
    def mySqrt(self, x: int) -> int:
        # O(logn) Binary Search Implementation.
        if x == 0: return 0
        elif x == 1: return 1
        
        l = 0
        r = x // 2
        while l <= r:
            mid = (l + r) // 2
            #print("mid:",mid, "mid^2:", mid*mid, "l:", l ,"r:", r)
            if mid * mid < x:
                l = mid + 1
                #print("l", l)
            elif mid *  mid > x:
                r = mid - 1
                #print("r", r)
            else:
                #print("returned mid:", mid)
                return mid
        #print("returned r:", r)
        return r