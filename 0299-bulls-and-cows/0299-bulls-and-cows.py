class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Brute Force O(n^3) Solution where you create 4 maps to count bulls and cows
        length = len(secret)
        bullsMap = list((guess[i] == secret[i] for i in range(length)))
        #print("BullsMap:", bullsMap)
        
        # Get secretMap pairs from false values in bulls map via a dictionary comprehension
        secretMap = {secret[i]: secret.count(secret[i]) for i in range(len(secret)) if not bullsMap[i]}
        #print("Secret Map:", secretMap)
        
        # Get cows map from false values in bulls map via a generator
        cowsMap = (index for index in range(len(bullsMap)) if not bullsMap[index])
        
        # Create bulls dictionary utilizing the bullsMap and a generator
        bulls = {}
        bullIndex = (index for index in range(len(bullsMap)) if bullsMap[index])
        for index in bullIndex:
            if secret[index] not in bulls:
                bulls[secret[index]] = 1
            else:
                bulls[secret[index]] += 1
        print("Bulls:", bulls)
        
        for key in bulls:
             if key in secretMap:
                secretMap[key] -= bulls[key]

        # Count remaining cows
        cowSum = 0
        for index in cowsMap:
            print(guess[index], secret[index])
            if guess[index] in secretMap and secretMap[guess[index]] > 0:
                secretMap[guess[index]] -= 1
                cowSum += 1
                
        return str(sum(bullsMap)) + "A" + str(cowSum) + "B"