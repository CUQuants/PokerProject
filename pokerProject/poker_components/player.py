class npcPlayer:
 def __init__(self, name):
    self.name = name
    self.hand = []

 def recieve_card(self, card):
   self.hand.append(card)

 def call(self):
   return
 
 def fold(self):
   return
 
 def raise_bet(self):
    return
 
# Turn function:  Called by table class and asks player to make a decisions
