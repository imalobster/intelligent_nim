class Board:
    def __init__(self, piles):
        self.piles = piles
        self.original_piles = piles
        self.original_max = max(self.original_piles)

    def updatePiles(self, piles):
        self.piles = piles

    def drawBoard(self):
        print("\n")
        def dObj(self, val, cur):
            if val >= cur:
                return "*"
            else:
                return " "

        for i in range(self.original_max, 0, -1):
            print("     |", end='')
            for val in self.piles:
                print(" {} |".format(dObj(self, val, i)), end='')
            print()

        print("PILE:  ", end='')
        for i in range(0, len(self.piles)):
            print("{}   ".format(i+1), end='')
        print()


