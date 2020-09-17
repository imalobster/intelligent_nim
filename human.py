class Human:
    def takeTurn(self, piles):
        print("It's your turn human!\nSelect which pile you would like to remove from, then the amount separated by a space:")
        
        while True:
            try:
                response = list(map(int, input().split()))
            except ValueError:
                print("[ERROR]: Please ensure you are only entering integers with no other characters. Try again:")
                continue

            if len(response) != 2:
                print("[ERROR]: Please ensure you are entering two values. Try again:")
                continue
                
            if response[0] < 1 or response[0] > len(piles):
                print("[ERROR]: There is no pile {}. Try again:".format(response[0]))
                continue

            if response[1] < 1 or response[1] > piles[response[0] - 1]:
                print("[ERROR]: Invalid amount for that pile. Try again:")
                continue

            else:
                return response[0] - 1, response[1]
    

    def victoryMessage(self):
        print("\nWe have a winner! The human has defeated the evil robot.")
