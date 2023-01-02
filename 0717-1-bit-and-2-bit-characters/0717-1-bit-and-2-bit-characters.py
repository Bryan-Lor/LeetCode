class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # O(n) Solution with sliding window technique. Run two pointers
        # throughout the list to determine if two bit or one bit.
        if len(bits) < 2: return True
        
        left = 0
        right = 1
        while right < len(bits) - 1:
            if bits[left] == 1:
                right += 2
                left = right -1
                if (right > len(bits) - 1):
                    right = len(bits) - 1
                    if (right - left == 1):
                        left = right
            else:
                right += 1
                left = right - 1
                
        if (bits[left] == 1):
            return False
        return True