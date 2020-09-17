from random import randint
from board import Board
from human import Human
from agent import Agent

class Nim:
    def __init__(self, n_objects):
        self.n_objects = 2 * n_objects + 1
        self.n_piles = randint(2,5)
        self.piles = []
        self.assignObjects()
        self.board = Board(self.piles)
        self.human = Human()
        self.agent = Agent()
        
        if (randint(0, 1) == 0):
            self.humanFirst = True
            print("Welcome to the game of Nim!\nThe player to go first has been randomly assigned to the human...")
        else:
            self.humanFirst = False
            print("Welcome to the game of Nim!\nThe player to go first has been randomly assigned to the agent...")

        input("When you are ready, press the enter key to begin: ")
        self.drawBoard()
        

    def assignObjects(self):
        for i in range(self.n_piles - 1):
            self.piles.append(randint(1, self.n_objects - sum (self.piles) - self.n_piles + i))
        self.piles.append(self.n_objects - sum(self.piles))


    def drawBoard(self):
        self.board.drawBoard()


    def handleTurn(self):
        if (self.humanFirst):
            if (self.playerTurn(self.human) or self.playerTurn(self.agent)):
                return True
        else:
            if (self.playerTurn(self.agent) or self.playerTurn(self.human)):
                return True
        return False


    def playerTurn(self, player):
        pile_no, object_no = player.takeTurn(self.piles)
        self.removeObjects(pile_no, object_no)
        self.board.updatePiles(self.piles)
        self.drawBoard()
        return self.checkWin(player)
            
    
    def removeObjects(self, pile_no, object_no):
        self.piles[pile_no] = self.piles[pile_no] - object_no


    def checkWin(self, player):
        if (sum(self.piles) == 0):
            player.victoryMessage()
            return True
        else:
            return False





