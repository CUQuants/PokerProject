from poker_components.cardDeck import CardDeck
from poker_components.player import Player

class Table:
    def __init__(self, name):
        self.pot = 0
        self.players = []
        self.public_cards = []
        self.active_players = 0
        self.current_bet = 0
        self.deck = CardDeck()
        # self.current_turn = 0
        
    def add_player(self, player):
        self.players.append(player)
        
    def deal_player(self, player):
        self.players[player].recieve_card(self.deck.deal())
        return
    
    def deal_public(self):
        self.public_cards.append(self.deck.deal())
        self.public_cards.append(self.deck.deal())
        self.public_cards.append(self.deck.deal())
        return
    
    def play(self, current_turn):
        
        
        if self.players[current_turn].folded is True:
            return
        
        if self.active_players == 1:
            print("Congratulations, " + str(self.players[current_turn].name) + "!")
            print("You won!")
            return
        
        
        curPlayer = self.players[current_turn]
        
        print("It is ", curPlayer.name, "'s turn.")
        print("Your hand is: ")
        for card in curPlayer.hand:
            print(card)
        
        print("You have " + str(curPlayer.balance) + " chips remaining.")
        print("The pot is " + str(self.pot) + " chips.")
        print("The current bet is " + str(self.current_bet) + " chips.")
        print("What would you like to do?")
        print("1. Call")
        print("2. Fold")
        print("3. Raise")
        print("4. Check")
        decision = input()
        
        while decision.isdigit() is False and decision != "1" and decision != "2" and decision != "3" and decision != "4":
            print("Invalid input.  Please try again.")
            decision = input()
        
        
        if decision == "1":
            if curPlayer.call(curPlayer.balance, self.current_bet) is False:
                self.play(current_turn)
            self.pot += self.current_bet
            
        elif decision == "2":
            print("You folded.")
            curPlayer.folded = True
            self.active_players -= 1
            
        elif decision == "3":
            if curPlayer.balance < self.current_bet:
                print("You do not have enough chips to raise.")
                self.turn()
            print("How much would you like to raise?")
            userInput = input()
            
            while userInput.isdigit() is False:
                print("Invalid input.  Please try again.")
                userInput = input()
                
            amount_raised = int(userInput)
    
            while int(amount_raised) < self.current_bet or int(amount_raised) > curPlayer.balance or int(amount_raised) < 1:
                print("Invalid input.  Please try again.")
                amount_raised = input()
                amount_raised = int(amount_raised)
                
            curPlayer.raise_bet(amount_raised)
            self.pot += amount_raised
            self.current_bet = amount_raised
            
        elif decision == "4":
            if self.current_bet == 0:
                curPlayer.check()
            else:
                print("You cannot check. Please choose another option.")
                self.play(current_turn)
            curPlayer.check()
        else:
            print("Invalid input.  Please try again.")
            self.play(current_turn)
        return