'''
Complete Blackjack from scratch
1)Use 4, 52 card decks and assign values
Remember you have K, Q , J = 10, and Ace is 1 or 11
2) Keep track of your score and dealers score (hits up until a value of 17)
3) Record if you want to hit or stay
4) Compare your final value to the dealer
5) Win or play again!

Classes: 7

class Player
class HumanPlayer(Player)
class Dealer(Player)

class Deck
class Card
class BlackjackHand

class BlackjackGame

Usecase:

player = HumanPlayer()
dealer = Dealer()
game = BlackjackGame(player, dealer)
game.play()

'''
import random

class Player:

    def __init__(self):
        self.new_hand()

    def new_hand(self):
        self.hand = BlackjackHand()

    def hit_or_stay(self, game):
        pass


class Dealer(Player):

    def __init__(self):
        super().__init__()

    def hit_or_stay(self, game):
        if self.hand.score <= 16:
            return 'h'
        elif self.hand.score == 17:
            if any(card.is_ace() and card.value == 11
                    for card in self.hand):
                return 'h'
        return 's'
class HumanPlayer(Player):

    def __init__(self):
        super().__init__()

    def play_again(self):
        while True:
            inp = input('Play again (y/n)? ')
            if not inp:
                continue
            elif inp.lower()[0] == 'y':
                return True
            elif inp.lower()[0] == 'n':
                return False

    def hit_or_stay(self, game):
        while True:
            inp = input('Hit or stay (h/s)? ')
            if not inp:
                continue
            elif inp.lower()[0] == 'h':
                return 'h'
            elif inp.lower()[0] == 's':
                return 's'
class Deck:

    def __init__(self):
        faces = [str(i) for i in range(2, 11)]
        faces.extend(['J', 'Q', 'K', 'A'])
        values = [i for i in range(2, 11)] + [10, 10, 10, 11]
        suits = ['♠','♥','♣','♦']
        self._deck = [
            Card(face, suit, val)
            for face, val in zip(faces, values) for suit in suits
        ]
        self.remaining = list(self._deck)

    def restart(self):
        self.remaining = list(self._deck)
        return self

    def shuffle(self):
        random.shuffle(self.remaining)
        return self

    def draw_without_replacement(self):
        if not self.remaining:
            return None
        i = random.randint(0, len(self.remaining) - 1)
        card = self.remaining[i]
        del self.remaining[i]
        return card

class Card:

    facedown = '???'

    def __init__(self, face, suit, value=None):
        self.faceup = False
        self.face, self.suit, self.value = face, suit, value

    def is_ace(self):
        return self.face == 'A'

    def __str__(self):
        return f'{self.face} {self.suit}' if self.faceup else self.facedown

class BlackjackHand:

    def __init__(self):
        self.cards = []

    def __str__(self):
        return ', '.join([str(card) for card in self.cards])

    def __getitem__(self, index):
        return self.cards[index]

    @property
    def score(self):
        return sum([card.value for card in self.cards])

    def deal(self, card, faceup=True):
        card.faceup = faceup
        self.cards.append(card)

class BlackjackGame:

    max_per_round = 16

    def __init__(self, player, dealer):
        self.deck = Deck()
        self.player = player
        self.dealer = dealer
        self.finished = False

    def play(self):
        while not self.finished:
            if self.play_round():
                print('You won!')
            else:
                print('The dealer won.')
            if not self.player.play_again():
                self.finished = True

    def initial_deal(self):
        self.player.hand.deal(self.deck.draw_without_replacement())
        self.dealer.hand.deal(self.deck.draw_without_replacement())
        self.player.hand.deal(self.deck.draw_without_replacement())
        self.dealer.hand.deal(
            self.deck.draw_without_replacement(), faceup=False)
    def print_status(self):
        print(f'Player: {self.player.hand}')
        print(f'Dealer: {self.dealer.hand}')

    def play_round(self):
        self.player.new_hand()
        self.dealer.new_hand()

        if len(self.deck.remaining) < self.max_per_round:
            self.deck.restart().shuffle()
        self.initial_deal()
        self.print_status()

        # Player plays.
        while self.player.hit_or_stay(self) == 'h':
            card = self.deck.draw_without_replacement()
            self.player.hand.deal(card)
            self.print_status()
            if self.player.hand.score > 21:
                # Search for an ace and convert to 1 if it exists.
                for c in self.player.hand:
                    if c.is_ace() and c.value == 11:
                        c.value = 1
            if self.player.hand.score > 21:
                break
        # Dealer plays.
        self.dealer.hand[1].faceup = True
        self.print_status()
        while self.dealer.hit_or_stay(self) == 'h':
            self.dealer.hand.deal(
                self.deck.draw_without_replacement())
            self.print_status()
            if self.dealer.hand.score > 21:
                break

        return (self.player.hand.score <= 21
            and (self.dealer.hand.score > 21
                or self.player.hand.score >
                self.dealer.hand.score))

player = HumanPlayer()
dealer = Dealer()
game = BlackjackGame(player, dealer)
game.play()
