

# ######################## Taner
   def status(self):
        # if player not choose STAND, take one more Card..
        if not Game.stand():
            self._cards_of_player = self._cards_of_player.append(DeckOfCards.deal_card())
        # if player is STAND, take one more Card to dealer..
        else:
            self._cards_of_dealer = self._cards_of_dealer.append(DeckOfCards.deal_card())
            Card(self._cards_of_dealer)
        # if players point is 21, the turn goes to dealer.
        if self._total_wins_player() == 21:
            self._cards_of_dealer = self._cards_of_dealer.append(DeckOfCards.deal_card())
        # if players point is over 21, then finish game.
        if self._total_wins_player() > 21:
            Game.finish_set()

    def stand(self):
        stand = input("For Stand Press 'S'...")
        if stand.lowercase() == "s":
            return True
        else:
            return False

# ######################## Taner
