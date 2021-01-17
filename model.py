import random

class Card():
    __colors = ["kupa", "špadi", "dinari", "baštoni"]
    __values = {
        1: 3,
        2: 1,
        3: 1,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        11: 1,
        12: 1,
        13: 1
        }

    def __init__(self, color, name):
        self.__name = name
        self.__color = color
    
    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def pointValue(self):
        return Card.__values[self.name]

    @property
    def rank(self):
        if self.name < 4:
            return self.name + 13
        else:
            return self.name

    @staticmethod
    def colors():
        return Card.__colors

    @staticmethod
    def values():
        return Card.__values

    @staticmethod
    def isValidCall(cards):
        validCalls = [
            ['Card(kupa, 1)', 'Card(špadi, 1)', 'Card(dinari, 1)', 'Card(baštoni, 1)'],
            ['Card(kupa, 1)', 'Card(špadi, 1)', 'Card(baštoni, 1)'],
            ['Card(kupa, 1)', 'Card(dinari, 1)', 'Card(baštoni, 1)'],
            ['Card(špadi, 1)', 'Card(dinari, 1)', 'Card(baštoni, 1)'],
            ['Card(kupa, 2)', 'Card(špadi, 2)', 'Card(dinari, 2)', 'Card(baštoni, 2)'],
            ['Card(kupa, 2)', 'Card(špadi, 2)', 'Card(baštoni, 2)'],
            ['Card(kupa, 2)', 'Card(dinari, 2)', 'Card(baštoni, 2)'],
            ['Card(špadi, 2)', 'Card(dinari, 2)', 'Card(baštoni, 2)'],
            ['Card(kupa, 3)', 'Card(špadi, 3)', 'Card(dinari, 3)', 'Card(baštoni, 3)'],
            ['Card(kupa, 3)', 'Card(špadi, 3)', 'Card(baštoni, 3)'],
            ['Card(kupa, 3)', 'Card(dinari, 3)', 'Card(baštoni, 3)'],
            ['Card(špadi, 3)', 'Card(dinari, 3)', 'Card(baštoni, 3)'],
            ['Card(kupa, 1)', 'Card(kupa, 2)', 'Card(kupa, 3)'],
            ['Card(špadi, 1)', 'Card(špadi, 2)', 'Card(špadi, 3)'],
            ['Card(dinari, 1)', 'Card(dinari, 2)', 'Card(dinari, 3)'],
            ['Card(baštoni, 1)', 'Card(baštoni, 2)', 'Card(baštoni, 3)']
        ]

        if cards in validCalls:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.color}"

    def __repr__(self):
        return f'{self.__class__.__name__}({self.color}, {self.name})'

class Deck():
    def __init__(self):
        self.__cards = []
        self.__populateDeck()

    def __populateDeck(self):
        cards = []

        for color in Card.colors():
            for i in range(1,8):
                cards.append(Card(color, i))
            for i in range(11,14):
                cards.append(Card(color, i))

        self.__cards = cards

    def shuffle(self):
        random.shuffle(self.__cards)

    def dealHands(self):
        hands = [[], [], [], []]

        for i in range(0,4):
            hands[i] = self.__cards[i*10:i*10+10]

        return hands
    
    def __str__(self):
        return ', '.join([str(x) for x in self.__cards])

class Team():
    def __init__(self, player0, player1):
        self.__players = (player0, player1)
        self.__points = 0
        self.__collectedCards = []
        player0.setTeam(self)
        player1.setTeam(self)

    @property
    def players(self):
        return self.__players
    
    @property
    def points(self):
        return self.__points

    @property
    def collectedCards(self):
        return self.__collectedCards

    def addPoints(self, value):
        self.__points += value

    def addCollectedCards(self, cards):
        self.__collectedCards.extend(cards)

class Player():
    def __init__(self, name):
        self.__name = name
        self.__hand = []
        self.__team = None

    @property
    def name(self):
        return self.__name

    @property
    def hand(self):
        return self.__hand

    @hand.setter
    def hand(self, value):
        self.__hand = value
    
    def playCard(self, choice):
        card = self.__hand.pop(choice)
        return card
    
    def setTeam(self, team):
        self.__team = team

    def __str__(self):
        return f'{self.name}'

class Human(Player):
    def __init__(self, name):
        super(Human, self).__init__(name)

class PC(Player):
    def __init__(self, name):
        super(PC, self).__init__('PC')
