import Random
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'. split()

# for r in RANKS:
    #for s in SUITE:
        #mycards.append((s,r))

class Deck():
    """
    This is the Deck class. creates a Deck of Cards
    """
    def __init__(self):
        print("Creating new Ordered Deck")
        self.allcards = [(s,r) for s SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFFLING")
        shuffle(self.allcards)

    def split_in_half(self):
        return(self.allcards[:26], self.allcards[26:])

class Hand():

    def __init__(self, cards):
        self.cards = cards
    def __str__(self):
        return "Contains {} cards".fornat(len(self.cards))
    def add(self, added_cards):
        self.cards.extended(added_cards)
    def remove_card(self):
        return self.cards.pop()

class Player():

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        for x in range(3):
            war_cards.append(self.hand.cards.pop())
        return war_cards

    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0

print("Welcome to War, let's begin..")

d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

#create both platers!
comp = Player("Computer", Hand(half1))

name = input("What is your name?")
user = Player(name, Hand(half2))
