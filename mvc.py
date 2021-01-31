import random, os

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
            {'kupa 1', 'špadi 1', 'dinari 1', 'baštoni 1'},
            {'kupa 1', 'špadi 1', 'baštoni 1'},
            {'kupa 1', 'špadi 1', 'dinari 1'},
            {'kupa 1', 'dinari 1', 'baštoni 1'},
            {'špadi 1', 'dinari 1', 'baštoni 1'},
            {'kupa 2', 'špadi 2', 'dinari 2', 'baštoni 2'},
            {'kupa 2', 'špadi 2', 'baštoni 2'},
            {'kupa 2', 'špadi 2', 'dinari 2'},
            {'kupa 2', 'dinari 2', 'baštoni 2'},
            {'špadi 2', 'dinari 2', 'baštoni 2'},
            {'kupa 3', 'špadi 3', 'dinari 3', 'baštoni 3'},
            {'kupa 3', 'špadi 3', 'baštoni 3'},
            {'kupa 3', 'špadi 3', 'dinari 3'},
            {'kupa 3', 'dinari 3', 'baštoni 3'},
            {'špadi 3', 'dinari 3', 'baštoni 3'},
            {'kupa 1', 'kupa 2', 'kupa 3'},
            {'špadi 1', 'špadi 2', 'špadi 3'},
            {'dinari 1', 'dinari 2', 'dinari 3'},
            {'baštoni 1', 'baštoni 2', 'baštoni 3'}
        ]


        if cards in validCalls:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.color} {self.name}"

    def __repr__(self):
        return f'{self.__class__.__name__}({self.color}, {self.name})'

class Deck():
    def __init__(self):
        self.__cards = self.__populateDeck()  #4

    def __populateDeck(self): #5
        cards = []

        for color in Card.colors():
            for i in range(1,8):
                cards.append(Card(color, i))
            for i in range(11,14):
                cards.append(Card(color, i))

        return cards

    def shuffle(self):
        random.shuffle(self.__cards)

    def dealHands(self):                            #7
        hands = [[], [], [], []]

        for i in range(0,4):                        # for x4
            hands[i] = self.__cards[i*10:i*10+10]   #8

        return hands                                #9
    
    def __str__(self):
        return ', '.join([str(x) for x in self.__cards])

class Team():
    __teams = []

    def __init__(self, check):
        self.__isHumansTeam = check
        self.__points = 0
        self.__collectedCards = []
        Team.__teams.append(self)

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
    
    @staticmethod
    def otherTeam(t1):
        return [t for t in Team.__teams if t != t1][0]

class Player():
    def __init__(self, name, team):
        self.__name = name
        self.__hand = []
        self.__team = team

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

    @property
    def team(self):
        return self.__team

    def isInHand(self, cards):
        for card in cards:
            if card not in self.hand:
                return False
        return True

    def __str__(self):
        return f'{self.name}'

class Human(Player):
    def __init__(self, name, team):       #5
        super(Human, self).__init__(name, team)

class PC(Player):
    __names = ["Darko", "Paško", "Siniša"]

    def __init__(self, team):     #3
        super(PC, self).__init__(f"AI {PC.__names.pop(random.randint(0,len(PC.__names))-1)}", team)

class View():
    def startGameOutput(self):
        self.clearTerminal()
        print(
            '''********************************************\n****************IGRA TREŠETA****************\n********************************************'''
        )

    def clearTerminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
            
    def nameInput(self):                        #6
        ime = ""

        while True:
            ime = input("Unesite vaše ime: ")   #7

            for letter in ime:
                if not letter.isalpha:
                    print("Niste unijeli pravilno ime(mora sadržavati samo slova)!")
                    continue
            
            return ime                          #8

    def gameLayoutOutput(self, game):       #4
        self.clearTerminal()
        self.playedCardsOutput(game.playedHand, game.firstPlayer, game.players)
        print('''\n********************************************\n''')
        self.handOutput(game.humanPlayer.hand)
        print('''\n********************************************\n''')

    def playedCardsOutput(self, playedCards, firstPlayer, players):
        outputList = [f'{str(player)}: ' for player in players]
        print('Odigrane karte po igraću su:')
        for i in range(0,4):
            card = str(playedCards[i + firstPlayer]) if i + firstPlayer < 4 else str(playedCards[i + firstPlayer - 4])
            if card == 'None':
                card = ''
            print(outputList[i + firstPlayer] + card if i + firstPlayer < 4 else outputList[i + firstPlayer - 4] + card)

    def handOutput(self, cards):
        print('Karte u vašoj ruci su:\n' + ', '.join([str(card) for card in cards]))

    def callInput(self, player):
        while True:
            answer = input("Želite li unijeti zvanje(\"DA\" ili \"NE\"): ").upper()

            if answer == "DA":
                cards =  input("Unesite željeno zvanje(karte odvojene zarezima i razmakom): ").lower().split(", ")
                if Card.isValidCall(set(cards)) and player.isInHand(cards):
                    player.team.addPoints(len(cards))
                    call = ""
                    if cards[0].name == cards[1].name:
                        if cards[0].name == 1:
                            if len(cards) == 3:
                                call = f"tri jedinice bez jedinice {[color for color in [Card.colors] if color not in [card.color for card in cards]][0]}"
                            else:
                                call = "četiri jedinice"
                        elif cards[0].name == 2:
                            if len(cards) == 3:
                                call = f"tri dvice bez dvice {[color for color in [Card.colors] if color not in [card.color for card in cards]][0]}"
                            else:
                                call = "četiri dvice"
                        else:
                            if len(cards) == 3:
                                call = f"tri trice bez trice {[color for color in [Card.colors] if color not in [card.color for card in cards]][0]}"
                            else:
                                call = "četiri trice"
                    else:
                        call = f"napola {cards[0].color}"

                    print(f"Igrač {str(player)} zove {call}")
                else:
                    print("Unijeli ste krivo zvanje, pokušajte ponovo.")
            elif answer == "NE":
                break
            else:
                print("Krivi unos, pokušajte ponovo.")
            
    def signInput(self, player):
        while True:
            answer = input("Želite li motirati(\"DA\" ili \"NE\"): ").upper()

            if answer == "DA":
                sign =  input("Unesite željeni mot(\"strišo\" ili \"tučem\"): ").lower()

                if sign == "strišo":
                    print(f"{player.name} motira strišo.") # briše se nakon odigrane karte
                    break
                elif sign == "tučem":
                    print(f"{player.name} motira tučem.") # briše se nakon odigrane karte
                    break
                else:
                    print("Unijeli ste krivi mot, pokušajte ponovo.")
            elif answer == "NE":
                break
            else:
                print("Krivi unos, pokušajte ponovo.")

    def playingCardInput(self, player):
        while True:
            answer = input("Unesite kartu koju želite odigrati: ").lower()
            strReprList = [str(card) for card in player.hand]

            print(answer, strReprList)
            if answer in strReprList:
                print(f"Odigrali ste kartu: {answer}.")
                return strReprList.index(answer)
            else:
                print("Unijeli ste krivu kartu, pokušajte ponovo.")
    
    def roundScoreOutput(self, t1, t2):
        self.clearTerminal()
        print(f"Do sada ste osvojili {t1.points} bodova, dok je protivnički tim osvojio {t2.points} bodova.")
        self.stop()


    def endGameOutput(self, team):
        if team.isHumansTeam:
            print(f"Pobijedili ste u ovoj igri {team.points}:{Team.otherTeam.points}.")
        else:
            print(f"Izgubili ste u ovoj igri {team.points}:{Team.otherTeam.points}.")

    def playedHandOutput(self, player):
        print(f"{player} je uzeo ruku.")

    def stop(self):
        input("Pritisnite enter za nastavak!")

    def AICallOutput(self, player, call):
        print(f'{player} zove {[card for card in call].join(", ")}')

class Game():
    def __init__(self):
        self.__view = View()    #2
        self.__deck = Deck()    #3
        self.__players = [None, None, None, None]
        self.__firstRound = True
        self.__firstHand = True
        self.__firstPlayer = -1
        self.__playedHand = [None, None, None, None]

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
    def firstRound(self):
        return self.__firstRound

    @property
    def playedHand(self):
        return self.__playedHand

    @property
    def humanPlayer(self):
        for player in game.players:
            if isinstance(player, Human):
                return player

    @property
    def firstHand(self):
        return self.__firstHand

    @firstHand.setter
    def firstHand(self, value):
        self.__firstHand = value

    @firstRound.setter
    def firstRound(self, value):
        self.__firstRound = value
        
    def playingTreseta(self):           #1
        self.view.startGameOutput()     #2
        self.playerEntry()              #3
        while True:                     # do while not check
            self.dealCards()            #4
            self.playRound()            #5
            check = self.scoring()      #6

            if not check:
                break

    def playerEntry(self):                                  #1
        humanTeam, AITeam = Team(True), Team(False)

        for i in range(0,3):                                # for x3
            if i == 1:
                self.__players[i] = PC(humanTeam)           #2 #3
            else:
                self.__players[i] = PC(AITeam)
        
        self.__players[3] = Human(self.view.nameInput(), humanTeam)    #4 #5 #6 #7 #8
    
    def dealCards(self):                                    #1
        if self.firstRound:                                 # firstRound
            self.firstPlayer = random.randint(0, 3)         # 
        else:                                               # else
            if self.firstPlayer == 3:                       # firstPlayer == 3
                self.firstPlayer == 0                       #4
            else:                                           # else
                self.firstPlayer += 1                       #5
        
        self.deck.shuffle()                                 #6
        
        for i, hand in enumerate(self.deck.dealHands()):    # for enumerate(deck.dealHands()) #7 #9
            self.players[i].hand = hand                     #10 #11

        self.firstHand = True

    def playRound(self):                                                #1
        while self.players[0].hand:                                     # exists card in hand #2 #3
            self.playHand()                                             #4

            if self.firstRound:
                self.firstRound = False
    
    def scoring(self):                                                  #1                            #1
        teams = (self.players[0].team, self.players[1].team)            #2                          #
        
        for team in teams:                                              #3
            team.addPoints(sum([card.pointValue for card in team.collectedCards])//3)
        self.players[self.firstPlayer].team.addPoints(1)

        if self.players[self.firstPlayer].team.isHumansTeam:
            self.view.roundScoreOutput(self.players[self.firstPlayer].team, Team.otherTeam(self.players[self.firstPlayer].team))
        else:
            self.view.roundScoreOutput(Team.otherTeam(self.players[self.firstPlayer].team), self.players[self.firstPlayer].team)
 
        if teams[0].points >= 41 or teams[1].points >= 41:
            if teams[0].points == teams[1].points:
                return True
            elif teams[0].points > teams[1].points:
                self.view.endGameOutput(teams[0])
                return False
            else:
                self.view.endGameOutput(teams[1])
                return False
        else:
            return True

    def playHand(self):
        for player in self.playersOrdered():
            if isinstance(player, Human):
                self.playCard(player)
            else:
                self.playCardAI(player)
        
        if self.firstHand:
            self.firstHand = False
        
        self.evaluateHand()

    def playCard(self, player):
        self.view.gameLayoutOutput(self)

        if self.firstHand:
            self.view.callInput(player)

        if player == self.players[self.firstPlayer] and not self.firstHand:
            self.view.signInput(player)

        playedCard = player.hand[self.view.playingCardInput(player)]
        self.playedHand[self.players.index(player)] = playedCard
        player.hand.remove(playedCard)

    def playCardAI(self, player):
        self.view.clearTerminal()

        if self.firstHand:
            calls = self.callAIOutput(player)

            if calls:
                for call in calls:
                    player.team.addPoints(len(call))
                    self.view.AICallOutput(self, player, call)
                    

        playedCard = self.cardAIOutput(player)
        self.playedHand[self.players.index(player)] = playedCard
        player.hand.remove(playedCard)

    def evaluateHand(self):
        self.view.gameLayoutOutput(self)
        maxRank = max([card.rank for card in self.playedHand if card.color == self.playedHand[self.firstPlayer].color])
        winningCard = [card for card in self.playedHand if card.rank == maxRank and card.color == self.playedHand[self.firstPlayer].color][0]
        self.firstPlayer = self.playedHand.index(winningCard)
        self.playersOrdered()[0].team.addCollectedCards(self.playedHand)
        self.__resetPlayedHand()
        self.view.playedHandOutput(self.players[self.firstPlayer])
        self.view.stop()

    def __resetPlayedHand(self):
        self.__playedHand = [None, None, None, None]

    def playersOrdered(self):
        players = []

        for i in range(0,4):
            players.append(self.players[self.firstPlayer + i if self.firstPlayer + i < 4 else self.firstPlayer + i - 4])
        
        return players

    def callAIOutput(self, player):
        calls = []
        callCounters = {"1": 0, "2": 0, "3": 0}
        for card in [card for card in player.hand]:
            if card.name == "1":
                callCounters["1"] += 1
            elif card.name == "2":
                callCounters["2"] += 1
            elif card.name == "3":
                callCounters["3"] += 1

        for i in range(1,4):
            if callCounters[str(i)] >= 3:
                calls.append([str(card) for card in player.hand if card.name == str(i)])
            
        if callCounters["1"] != 0 and callCounters["2"] != 0 and callCounters["3"] != 0:
            for color in Card.colors:
                possibleCall = [card for card in player.hand if (card.color == color and (card.name == 1 or card.name == 2 or card.name == 3))]
                if len(possibleCall) == "3":
                    calls.append([str(card) for card in possibleCall])

        return calls

    def cardAIOutput(self, player):
        if [True for card in self.playedHand if card is not None]:
            cardsInColor = [card for card in player.hand if card.color == self.playedHand[self.firstPlayer].color]

            if cardsInColor:
                return random.choice(cardsInColor)

        return random.choice(player.hand)



        

game = Game()           #1
game.playingTreseta()   #6