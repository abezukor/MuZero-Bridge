from enum import Enum

class Suits(Enum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS=2
    SPADES=3
    NOTRUMP=4
    def suitChar(self):
        suitchars = {
            "CLUBS": "♣",
            "DIAMONDS": "♦",
            "HEARTS": "♥",
            "SPADES": "♠",
            "NOTRUMP": "NT"
        }
        return suitchars[self._name_]

class Values(Enum):
    TWO= 2
    THREE= 3
    FOUR=4
    FIVE=5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def valueChar(self):
        valuesDict = {
            "TWO": '2',
            "THREE": '3',
            "FOUR": '4',
            "FIVE": '5',
            "SIX": '6',
            "SEVEN": '7',
            "EIGHT": '8',
            "NINE": '9',
            "TEN": '10',
            "JACK": 'J',
            "QUEEN": 'Q',
            "KING" : 'K',
            "ACE": 'A'
        }
        return valuesDict[self.name]
class Card:
    def __init__(self,suit,value):
        self.value = value
        self.suit = suit
    def __repr__(self):
        return "<Card: {} of {}>".format(self.value.name, self.suit.name)
    def __str__(self):
        return "{}{}".format(self.value.valueChar(), self.suit.suitChar())
    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value
    def __ne__(self,other):
        return not self==other
    def getActionNum(self):
        return 4*self.suit.value +self.value.value -2