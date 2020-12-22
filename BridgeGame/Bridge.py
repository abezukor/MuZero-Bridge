import numpy
from enum import Enum
import random

from Card import Suits, Values, Card

class Positions(Enum):
    NORTH = 0
    SOUTH = 2
    EAST = 1
    WEST = 3
    def next(self):
        return Positions((self.value+1)%4)
class GameStates(Enum):
    BIDDING = 0
    PLAYING = 1
class Player:
    def __init__(self,position,hand):
        self.hand = hand
        self.position = position
    def __repr__(self):
        return "<Player at {} with hand {}>".format(self.position.name, ", ".join(str(c) for c in self.hand))
    
class Trick:
    def __init__(self,trump):
        self.trump = trump
        self.suit = None
        self.cards = {}
    def addCard(self,pos,card):
        if(self.suit==None):
            self.suit=card.suit
        self.cards[pos] = card
    def winner(self):
        trumpplayers = []
        for k in self.cards:
            v = self.cards[k]
            if v.suit==self.trump:
                trumpplayers.append((k,v))
        #print("Trump Players: ", trumpplayers)
        if(trumpplayers):
            return max(trumpplayers, key=lambda item: item[1].value.value)[0]
        
        suitplayers = []
        for k in self.cards:
            v = self.cards[k]
            if v.suit==self.suit:
                suitplayers.append((k,v))
        #print("Suit Players: ", suitplayers)
        if(suitplayers):
            return max(suitplayers, key=lambda item: item[1].value.value)[0]
    def playerActions(self,player):
        if any([c.suit==self.suit for c in player.hand]):
            return [c for c in player.hand if c.suit==self.suit]
        return player.hand    
class Bridge:
    def __init__(self):
        self.currentPlayer = Positions.NORTH
        self.NSpoints = 0
        self.NSgames = 0
        self.EWpoints = 0
        self.EWgames = 0
        self.playedCards = []
        self.gameState = GameStates.BIDDING
        self.dealHands()
    def dealHands(self):
        cards = []
        for suitname, suitmember in Suits.__members__.items():
            for valuename, valuemember in Values.__members__.items():
                if(suitname!="NOTRUMP"):
                    cards.append(Card(suitmember,valuemember))
        random.shuffle(cards)
        self.players = {
            Positions.NORTH: Player(Positions.NORTH, cards[0:13]),
            Positions.EAST: Player(Positions.EAST, cards[13:26]),
            Positions.SOUTH: Player(Positions.SOUTH, cards[26:39]),
            Positions.WEST: Player(Positions.WEST, cards[39:52])
        }
        print(self.players)
    def to_play(self):
        return int(self.currentPlayer in (Positions.NORTH,Positions.SOUTH))
    def legal_actions(self):
        if(self.gameState == GameStates.PLAYING):
            return [c.getActionNum() for c in self.trick.playerActions(self.currentPlayer)]
