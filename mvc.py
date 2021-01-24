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
    def __init__(self, check):
        self.__isHumansTeam = check
        self.__points = 0
        self.__collectedCards = []

    @property
    def isHumansTeam(self):
        return self.__isHumansTeam
    
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
        super(Human, self).__init__("")

    @name.setter
    def name(self, value):
        self.name = value

class PC(Player):
    def __init__(self, name):
        super(PC, self).__init__("PC")

class View():
    def startGameOutput(self):
        print(
            '''********************************************\n****************IGRA TREŠETA****************\n********************************************'''
        )
    
    def nameInput(self):
        ime = ""

        while True:
            ime = input("Unesite vaše ime: ")

            for letter in ime:
                if not letter.isalpha:
                    print("Niste unijeli pravilno ime(mora sadržavati samo slova)!")
                    continue
            
            return ime

    def gameLayoutOutput(self):
        View.playedCardsOutput(["", "", "3 kupa", "4 špadi"], 2)
        print('''\n********************************************\n''')
        View.handOutput(["", "", "3 kupa", "4 špadi"])
        print('''\n********************************************\n''')
        View.logOutput()

    def playedCardsOutput(self, playedCards, firstPlayer):
        outputList = ['Igrać s lijeva: ', 'Vaš par: ', 'Igrać s desna: ', 'Vi: ']
        print('Odigrane karte po igraću su:')
        for i in range(0,4):
            print(outputList[i + firstPlayer] + playedCards[i + firstPlayer] if i + firstPlayer < 4 else outputList[i + firstPlayer - 4] + playedCards[i + firstPlayer - 4])

    def handOutput(self, cards):
        print('Karte u vašoj ruci su:\n' + ', '.join(cards))
    
    def logOutput(self):
        pass

    def callInput(self):
        while True:
            answer = input("Želite li unijeti zvanje(\"DA\" ili \"NE\"): ")
            cardList = []

            if answer == "DA":
                cardList =  input("Unesite željeno zvanje(karte odvojene zarezima i razmakom): ").split(", ")
                if Card.isValidCall(cardList):
                    # fali interakcija
                    print("Vaše zvanje je uneseno!")
                else:
                    print("Unijeli ste krivo zvanje, pokušajte ponovo.")
            elif answer == "NE":
                break
            else:
                print("Unijeli ste krivo zvanje, pokušajte ponovo.")
            
    def signInput(self):
        while True:
            answer = input("Želite li motirati(\"DA\" ili \"NE\"): ")

            if answer == "DA":
                sign =  input("Unesite željeni mot(\"strišo\" ili \"tučem\"): ")

                if sign == "strišo":
                    # fali interakcija
                    print("Vaš mot je unesen!")
                    break
                elif sign == "tučem":
                    # fali interakcija
                    print("Vaš mot je unesen!")
                    break
                else:
                    print("Unijeli ste krivi mot, pokušajte ponovo.")
            elif answer == "NE":
                break
            else:
                print("Unijeli ste krivi mot, pokušajte ponovo.")

    def playingCardInput(self):
        while True:
            answer = input("Unesite kartu koju želite odigrati: ")

            if answer in player.hand:
                # fali interakcija
                print(f"Odigrali ste kartu: {answer}.")
                break
            else:
                print("Unijeli ste krivu kartu, pokušajte ponovo.")
    
    def roundScoreOutput(self):
        print(f"U ovoj rundi ste osvojili {""} bodova, dok je protivnički ti osvojio {""} bodova.")

    def endGameOutput(self):
        if "winner":
            print(f"Pobijedili ste u ovoj igri {""}:{""}.")
        else:
            print(f"Izgubili ste u ovoj igri {""}:{""}.")

class Game():
    def __init__(self):
        self.__view = View()
        self.__deck = Deck()
        self.__teams = None
        self.__players = (None, None, None, None)
        self.__firstRound = True
        self.__firstPlayer = -1

    @property
    def view(self):
        return self.__view
    
    @property
    def deck(self):
        return self.__deck

    @property
    def players(self):
        return self.__players

    @property
    def firstPlayer(self):
        return self.__firstPlayer

    @firstPlayer.setter
    def firstPlayer(self, value):
        self.__firstPlayer = value
    
    @property
    def teams(self):
        return self.__teams
        
    def playingTreseta(self):
        self.view.startGameOutput()
        self.playerEntry()
        self.dealCards()
        self.playRound()
        self.scoring()

    def playerEntry(self):
        for i in range(0,3):
            self.__players[i] = PC()
        
        self.__players[3] = Human(self.view.nameInput())

    
    def dealCards(self):
        if self.__firstRound:
            self.firstPlayer = random.randint(0, 3)
            self.__firstRound = False
        else:
            if self.firstPlayer == 3:
                self.firstPlayer == 0
            else:
                self.firstPlayer += 1
        
        self.deck.shuffle()
        
        for i, hand in enumerate(self.deck.dealHands()):
            self.players[i].hand = [hand]

    def playRound(self):
        if True in [True for player in self.players if player.hand]:
            self.playHand()
        else:
            self.scoring()
    
    def scoring(self):
        pass

    def playHand(self):
        pass

    def playCard(self):
        pass

    def evaluateHand(self):
        pass



def terminal_mani():
    import os

    print("je je")
    h = input("asdasd: ")

    if h:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    print("DA")