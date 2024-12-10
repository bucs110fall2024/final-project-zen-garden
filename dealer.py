from deck import Deck
class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.hnd = [self.deck.deal(), self.deck.deal()]
        self.scre = self.total()
        
    def total(self):
        score = 0
        ace_count = 0
        for card in self.hnd:
            value = card.split()[0]
            score += self.deck.card_values[value]
            if value == 'A':
                ace_count += 1
        while score > 21 and ace_count:
            score -= 10
            ace_count -= 1
        return score
    
    def hit(self):
        self.hnd.append(self.deck.deal())
        self.scre = self.total()
            
    def hand(self):
        return self.hnd
    
    def score(self):
        return self.scre
    
    def hand1(self):
        return self.hnd[:1]