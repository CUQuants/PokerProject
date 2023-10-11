class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __lt__(self, other): 
        return ((self.rank) <  other.rank) 
  
    def __gt__(self, other): 
        return ((self.rank) >  other.rank)
  
    def __le__(self, other): 
        return ((self.rank) <=  other.rank) 
  
    def __ge__(self, other): 
        return ((self.rank) >=  other.rank) 
  
    def __eq__(self, other): 
        return (self.rank == other.rank)

    def __repr__(self):
        return str(self.rank)+" of "+ str(self.suit)
