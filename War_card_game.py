from random import shuffle
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
class Deck:
    def __init__(self):
        print("Creating New Ordered Deck")
        self.allcards = [(s, r) for s in SUITE for r in RANKS]
    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)
    def cut(self):
        return (self.allcards[:26], self.allcards[26:])
class Hand:
    def __init__(self, cards):
        self.cards = cards
    def __str__(self):
        return f"have {len(self.cards)} cards"
    def add(self, added_cards):
        self.cards.extend(added_cards)
    def remove(self):
        return self.cards.pop(0)
class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    def draw(self):
        drawn_card = self.hand.remove()
        print(f"{self.name} has placed: {drawn_card}")
        print("\n")
        return drawn_card
    def war_card(self):
        war_cards = []
        if len(self.hand.cards) < 1:
            return war_cards
        else:
            war_cards.append(self.hand.remove())
            return war_cards
    def not_empty(self):
        return len(self.hand.cards) != 0
def init():
    print("Welcome to War, Let's begin!")
    # create, shuffle and cut the deck in half
    d = Deck()
    d.shuffle()
    half1, half2 = d.cut()
    
    round_count = 0
    war_count = 0
    
    comp = Player("Computer", Hand(half1))
    name = input("Player! What is your name? ")
    play = Player(name, Hand(half2))
    
    # Game started
    while comp.not_empty() and play.not_empty():
        round_count += 1
        print("It is time for a new round!")
        print("Here are the current standing: ")
        print(f"{play.name} has {len(play.hand.cards)} cards")
        print(f"{comp.name} has {len(comp.hand.cards)} cards")
        print("Both players placed a card!")
        print("\n")
        
        # craete a variable for the cards on the table
        table_cards = []
        
        # each player draw a card
        p_card = play.draw()
        c_card = comp.draw()
        
        # put the card on the table
        table_cards.append(p_card)
        table_cards.append(c_card)
        
        # chack to see if there is a War
        war = False
        if p_card[1] == c_card[1]:
            war = True
        while war:
            war_count += 1
            print("It is a war!")
            print("Each player remove one cards 'face down' and then one card 'face up'")
            table_cards.extend(play.war_card())
            table_cards.extend(comp.war_card())
            
            # draw card again
            p_card = play.draw()
            c_card = comp.draw()
            
            # add cards on the table
            table_cards.append(p_card)
            table_cards.append(c_card)
            
            # check to see if another war occured
            if p_card[1] == c_card[1]:
                continue
            else:
                war = False
        
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(f"{play.name} has the higher card, adding to hand.")
            play.hand.add(table_cards)
        else:
            print(f"{comp.name} had the higher card, adding to hand.")
            comp.hand.add(table_cards)
    print(f"Great Game! it lasted: {round_count} rounds")
    print(f"War occured: {war_count} times.")

init()