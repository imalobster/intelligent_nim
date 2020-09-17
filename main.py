from nim import Nim

print("[INFO]: Starting game of Nim")

n = 5
game = Nim(n)
while True:
    if (game.handleTurn()):
        break
    


