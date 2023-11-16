

class Player:
  def __init__(self, name: str):
    self.name = name
    self.hand = []
    self.balance = 1000
    self.folded = False

  def recieve_card(self, card):
   self.hand.append(card)

  def call(self, balance, curBet):
    if balance < curBet:
      print("You do not have enough chips to call.")
      return False
    if curBet == 0:
      print("You can't call when there is no bet.")
      return False
    print("You called.")
    balance -= curBet
    return True
 
  def raise_bet(self, amount_raised: int):
    amount_raised = int(amount_raised)
    print("You raised " + str(amount_raised) + " chips.")
    self.balance -= amount_raised

  def check(self, table): 
    print("You checked.")
 
