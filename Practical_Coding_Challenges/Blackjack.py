'''
Complete Blackjack from scratch
1)Use 4, 52 card decks and assign values
Remember you have K, Q , J = 10, and Ace is 1 or 11
2) Keep track of your score and dealers score (hits up until a value of 17)
3) Record if you want to hit or stay
4) Compare your final value to the dealer
5) Win or play again!

'''

# Blackjack
# 4 types of every card (one for each suit)
# K 5 A 7
# 9 8

class Game:
  def __init__(self):
    self.finished = False

  def play(self, dealer, player):
    # TODO: Fix the handling of aces, so their value changes to 1 if a value of 11 would go over 21

    def print_hands(player, dealer):
      print(f'player: {player.hand}')
      print(f'dealer: {dealer.hand}')

    # sequence of hands
    # initialize a deck (deck prevents duplicate cards)
    deck = Deck()
    while True:
      # deal to players
      # each player receives a hand
      # deck.deal(dealer, player) would be fine too
      dealer.initial_deal(deck, player)
      # show initial cards
      print_hands(dealer, player)
      # loop while not finished
      while not self.finished:
      # ask player if they want to hit or stay
        if player.hit_or_stay() == 'hit':
          dealer.deal(deck, player)
          print_hands(dealer, player)
          # check if player lost
          if player.hand.lost():
            print('You lost!')
            self.finished = True
        else:
          # player has set self.has_stayed = True
          pass
        # ask dealer if they want to hit or stay (deterministic - there's a rule)
        if dealer.hit_or_stay() == 'hit':
          # deal card
          # dealer has set self.has_stayed = True
          dealer.deal(deck, dealer)
          print_hands(dealer, player)
          # check if dealer lost
          if dealer.hand.lost():
            print('You win!')
            self.finished = True
        if player.has_stayed and dealer.has_stayed:
          if player.hand.score > dealer.hand.score:
            print('You win!')
          else:
            print('You lost!')
          self.finished = True

class Deck:
  def __init__(self):
    self.cards = self.full_deck()

  def full_deck(self):
    faces = [str(i) for i in range(2, 11)]
    faces += ['J', 'Q', 'K', 'A']
    return [Card(suit, face) for suit in ['C', 'D', 'S', 'H'] for face in faces]

  def choose_card_without_replacement(self):
    # TODO: Implement
    pass

class Suit:
  # clubs, diamonds, etc.
  pass

class Card:
  def __init__(self, suit, face, value):
    self.suit = suit
    self.face = face
    self.value = value  # TODO: Implement default value based on suit and face

  def __str__(self):
    return f'{self.suit}{self.face}'

class Hand:
  """
  cards that a player has
  """
  def __init__(self, cards=[]):
    self.cards = cards
    self.value = None

  def __str__(self):
    return ' '.join([str(card) for card in self.cards])

  def receive_card(self, card):
    self.cards.append(card)

  @property
  def score(self):
    return sum([card.value for card in self.cards])


class Player:
  def __init__(self, hand=None):
    self.hand = hand
    self.has_stayed = False

  def receive_card(self, card):
    self.hand.receive_card(card)

  def hit_or_stay(self):
    """
    return whether the player wants to hit or stay (receive a card or not)
    """
    # TODO: Implement
    pass

class Dealer(Player):
  def initial_deal(self, deck, player):
    # choose cards from the deck
    dealer_hand = Hand([deck.choose_card_without_replacement() for _ in range(2)])
    player_hand = Hand([deck.choose_card_without_replacement() for _ in range(2)])
    # give them to the players
    self.has_stayed = False
    player.has_stayed = False

  def deal(self, deck, player):
    # one card to one player
    card = deck.choose_card_without_replacement()
    player.receive_card(card)

class HumanPlayer(Player):
  # TODO: Implement
  pass

class AIPlayer(Player):
  pass

if __name__ == '__main__':
  g = Game
  dealer = Dealer()
  human = HumanPlayer()
  g.play(dealer, human)
