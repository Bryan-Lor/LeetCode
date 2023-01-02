class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Checks if the word is all upper, all lower, or capitalized. Then return
        # the respective boolean value.
        
        if (word == word.upper() or word == word.lower() or word == word.capitalize()):
            return True
        return False