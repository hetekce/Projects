import random


class Card:
    # constants are written always with CAPITAL LETTERS
    FACES = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    # Ace = [1, 11] # Has been reconsidered
    Values = {'Ace': 11, 'Jack': 10, 'Queen': 10, 'King': 10}

    def __init__(self):
        """Initialize a Card with a face and suit."""
        pass


class DeckOfCards:
    """DeckOfCards class represents a deck of Cards."""
    def __init__(self):
        """Initialize the deck."""
        self._deck = []

    def card_distribute(self, ard):
        while True:
            random_face = random.choice(ard.FACES)
            random_suit = random.choice(ard.SUITS)
            kart = [random_face, random_suit]
            if kart not in self._deck:
                self._deck.append(kart)
                break
            else:
                continue
        return self._deck[-1]


class Game:
    def __init__(self):
        """initialize a game class to play the game according to the rules"""

        self._point_of_dealer = 0
        self._point_of_player = 0
        self._cards_of_player = []
        self._cards_of_dealer = []
        self._points = []
        self._total_wins_player = 0
        self._total_wins_dealer = 0
        self._total_ties = 0
        self._hand = False
        self._black = False
        self._close = False

    def show_players_cards(self):

        print(f'the total value of player is {self._point_of_player}, '
              f'the cards of player are {self._cards_of_player}')

    def show_dealer_cards(self):

        if not self._hand:
            print(f'the first card of dealer is {self._cards_of_dealer[0]}')
        else:
            print(f'total value of dealer is {self._point_of_dealer},'
                  f'the cards of dealer are {self._cards_of_dealer}')

    def sum_of_cards_values(self, ard):
        self._point_of_player = 0
        self._point_of_dealer = 0
        for name, suit in self._cards_of_player:
            if type(name) != int:
                name = ard.Values[name]
                self._point_of_player += name
                # We are evaluating the value and then set Ace as 1
                if name == "Ace" and self._point_of_player > 21:
                    self._point_of_player -= 10
            else:
                self._point_of_player += name

        for name, suit in self._cards_of_dealer:
            if type(name) != int:
                name = ard.Values[name]
                self._point_of_dealer += name
                if name == "Ace" and self._point_of_player > 21:
                    self._point_of_player -= 10
            else:
                self._point_of_dealer += name
        self._points = [self._point_of_player, self._point_of_dealer]
        # return self._points

    def card_values_total(self):
        return self._points

    def card_names(self):
        return [self._cards_of_player, self._cards_of_dealer]

    def first_distribution(self, decks, ard):
        for i in range(2):
            self._cards_of_player.append(decks.card_distribute(ard))
            self._cards_of_dealer.append(decks.card_distribute(ard))
            self.sum_of_cards_values(ard)

    def black_jack_control(self):

        if self.card_values_total()[0] == 21:
            return True
        else:
            self._black = True
            return False

# ######################## Taner
    def status(self, decks, ard):
        # if player not choose STAND, take one more Card..
        if not self._hand:
            if not self.stand():
                self._cards_of_player.append(decks.card_distribute(ard))
                self.sum_of_cards_values(ard)
                self.show_players_cards()
                self.show_dealer_cards()
                if self._point_of_player <= 20:
                    return True
            else:
                return True
        # if player is STAND, take one more Card to dealer..
        else:
            if self._point_of_dealer <= self._point_of_player and self._point_of_dealer < 17:
                self._cards_of_dealer.append(decks.card_distribute(ard))
                self.sum_of_cards_values(ard)
                self.show_players_cards()
                self.show_dealer_cards()
                return True
            else:
                self.finish_set(decks)
                return False
                # if players point is 21, the turn goes to dealer.
        if self._point_of_player == 21 and self._point_of_dealer == 21:
            self.finish_set(decks)
            return False

        # if players point is over 21, then finish game.
        elif self._point_of_player > 21:
            self.finish_set(decks)
            return False

        elif self._point_of_dealer > 21:
            self.finish_set(decks)
            return False

        elif self._point_of_dealer > self._point_of_player and self._hand:
            self.finish_set(decks)
            return False

        else:
            self.finish_set(decks)
            return False
# ######################## Taner

    def __repr__(self):
        """Return string representation for repr()."""
        return f"Points(Player='{self._point_of_player}', Dealer='{self._point_of_dealer}')"

    def __str__(self):
        """Return string representation for str()."""
        return f'{self._point_of_player} of {self._point_of_dealer}'

    def start_game(self):

        print("Welcome To BlackJack")
        while True:
            self.black_jack_control()
            self.sum_of_cards_values()
            self.show_players_cards()
            self.show_dealer_cards()
            self.stand()
            while self.status():
                self.status()
            self.finish_game()

        # print(f'Cards of Player: %s ' % self._cards_of_player,
        #      f'\n Cards of Dealer: %s ' % self._cards_of_dealer)

    def finish_game(self):
        decision = input("Would you like to play one more time: Y/N")
        if decision.lower() == "y":
            return False
        else:
            self._close = True
            return True

    def print_results(self):
        if self._close:
            print("\n******************************************")
            print("\nThank you for playing with us\n")
            print(f' number of wins of player: %s' % self._total_wins_player,
                  f'\n number of wins of dealer: %s' % self._total_wins_dealer,
                  f'\n number of ties are: %s' % self._total_ties)
            print("\n******************************************\n")
            if self._total_wins_player > self._total_wins_dealer:
                print("Player defeated the dealer")
            else:
                print("Dealer defeated the player")
        else:
            print(f'Point of Player is: %s ' % self._point_of_player)
            print(f'Point of Dealer is: %s' % self._point_of_dealer)

    def stand(self):
        decision = input("For Stand Press 'S'...or to continue press any key")
        if decision.lower() == "s":
            self._hand = True
            return True
        else:
            return False

    def finish_set(self, deck):
        self.print_results()
        if self.black_jack_control() and not self._black:
            if self.card_values_total()[1] < 21:
                print("*************************************")
                print("Congratulations! You got a Blackjack!\n")
                print("*************************************")
                self._total_wins_player += 1
            else:
                print("NO WINNER! TIE")
                self._total_ties += 1
        elif self._point_of_player == 21 and self._point_of_dealer <= 21:
            if self._point_of_player > self._point_of_dealer:
                print("Congratulations. Your score is higher than the dealer. You win\n")
                self._total_wins_player += 1
            else:
                print("NO WINNER! TIE")
                self._total_ties += 1
        elif self._point_of_dealer == 21 and self._point_of_player <= 21:
            if self._point_of_player < self._point_of_dealer:
                print("Sorry. Your score isn't higher than the dealer. You lose.\n")
                self._total_wins_dealer += 1
            else:
                print("NO WINNER! TIE")
                self._total_ties += 1
        elif self._point_of_player > 21:
            print("Sorry. You busted. You lose.\n")
            self._total_wins_dealer += 1
        elif self._point_of_dealer > 21:
            print("Dealer busts. You win!\n")
            self._total_wins_player += 1
        elif self._point_of_dealer > 16:
            if self._point_of_player < self._point_of_dealer:
                print("Sorry. Your score isn't higher than the dealer. You lose.\n")
                self._total_wins_dealer += 1
            elif self._point_of_player > self._point_of_dealer:
                print("Congratulations. Your score is higher than the dealer. You win\n")
                self._total_wins_player += 1
            else:
                print("NO WINNER! TIE")
                self._total_ties += 1
        elif self._point_of_player < self._point_of_dealer:
            print("Sorry. Your score isn't higher than the dealer. You lose.\n")
            self._total_wins_dealer += 1
        elif self._point_of_player > self._point_of_dealer:
            print("Congratulations. Your score is higher than the dealer. You win\n")
            self._total_wins_player += 1
        elif self._point_of_player == self._point_of_dealer:
            print("NO WINNER! TIE")
            self._total_ties += 1

        self._point_of_dealer = 0
        self._point_of_player = 0
        self._cards_of_player = []
        self._cards_of_dealer = []
        self._hand = False
        self._black = False
        self._close = False
        deck._deck = []

# if __name__ == "__main__":
#    g = Game()
#    g.play()


game1 = Game()
decks1 = DeckOfCards()
cards1 = Card()
print("Welcome To BlackJack")
while True:
    game1.first_distribution(decks1, cards1)
    if game1.black_jack_control():
        game1.finish_set(decks1)
        if game1.finish_game():
            game1.print_results()
            break
    else:
        game1.show_players_cards()
        game1.show_dealer_cards()
        while game1.status(decks1, cards1):
            pass
        if game1.finish_game():
            game1.print_results()
            break



