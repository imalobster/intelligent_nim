class Agent:
    def takeTurn(self, piles):
        input("Agent turn, press the enter to allow it to make its move: ")

        currentNimSum = self.FindXOR(piles)

        if (currentNimSum == 0):
            # Agent realises it is in a losing position and seeks to delay game by removing only 1 object from largest stack
            print("{} {}".format(piles.index(max(piles)) + 1, 1))
            return piles.index(max(piles)), 1
        else:
            for i in range(0, len(piles)):
                # If pile has 0 objects remaining, skip
                if (piles[i] < 1):
                    continue
                # Find any pile whose size XOR currentNimSum is less than pile size, then reduce to get balanced
                if (piles[i] ^ currentNimSum) < piles[i]:
                    reduceBy = piles[i] - (piles[i] ^ currentNimSum)
                    print("{} {}".format(i+1, reduceBy))
                    return i, reduceBy


    def FindXOR(self, piles):
        # Remove zeros from piles list
        tempList = [pile for pile in piles if pile > 0]

        if len(tempList) == 1:
            return tempList[0]
        else:
            return tempList[-1] ^ self.FindXOR(tempList[:-1])


    def victoryMessage(self):
        print("\nHumanity is doomed, the agent has won the game.")