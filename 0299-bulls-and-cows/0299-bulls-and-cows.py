class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        length = len(secret)
        bullsMap = list((guess[i] == secret[i] for i in range(length)))
        print("BullsMap:", bullsMap)
        
        # Get secretMap pairs from false values in bulls map via a dictionary comprehension
        secretMap = {secret[i]: secret.count(secret[i]) for i in range(len(secret)) if not bullsMap[i]}
        print("Secret Map:", secretMap)
        
        # Get cows map from false values in bulls map via a generator
        cowsMap = (index for index in range(len(bullsMap)) if not bullsMap[index])
        #print("Cows Map:", cowsMap)
        
        bulls = {}
        bullIndex = (index for index in range(len(bullsMap)) if bullsMap[index])
        for index in bullIndex:
            if secret[index] not in bulls:
                bulls[secret[index]] = 1
            else:
                bulls[secret[index]] += 1
        print("Bulls:", bulls)
        
        # if bulls:
        #     secretMap = {key: secretMap[key] - bulls[key] for key in secretMap.keys()}
        #     print("RES:",secretMap)
        for key in bulls:
             if key in secretMap:
                secretMap[key] -= bulls[key]

        
        cowSum = 0
        for index in cowsMap:
            print(guess[index], secret[index])
            if guess[index] in secretMap and secretMap[guess[index]] > 0:
                print(True, guess[index], index, secretMap[guess[index]])
                secretMap[guess[index]] -= 1
                print("Secret Map:", secretMap)
                cowSum += 1
        print("Cow Sum:", cowSum)
        return str(sum(bullsMap)) + "A" + str(cowSum) + "B"