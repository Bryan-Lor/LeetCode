class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # O(n) Solution with sliding window technique. Run two pointers
        # throughout the list and compare left pointer to determine one or two bit
        if len(bits) == 1: return True
        left = 0
        right = 1
        while right < len(bits) - 1:
            if bits[left] == 1:
                right += 2
                left += 2
                if (right > len(bits) - 1):
                    right = len(bits) - 1
            else:
                right += 1
                left += 1
                
        return (bits[left] != 1)