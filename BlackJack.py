import random

print("Welcome to the BlackJack")

"""Rules of the game
1 -Blackjack oyununda amaç 21`i geçmeden krupiyeden daha yüksek bir skoru elde etmektir.
2- Papaz kız, vale kartlarının sayılasal değeri 10`dur.
3- As kartının sayısal değeri 1 ya da 11 dir.
4- Oyunun başında, kurupiye oyunculara ve kendine 2 kart verir.
5- Oyuncuların kartları açıktır ancak krupiyerin ilk kartı kapalı (Hole kart) ikinci kartı açıktır.
6- Oyuncunun aldığı ilk iki karttan biri 10 değerinde ve ikinci kart As ise oyuncu Blackjack yapmış olur ve otomatik olarak oyunu kazanır.
7- Eğer Blackjack durumu söz konusu değilse oyuncular kartlarının sayısal toplamının değerine göre 21`e yaklaşmak için 21`i geçmemek koşulu ile kart istemeye devam edebilirler (hit) ya da oyuncu elinin yeteri kadar güçlü olduğunu düşünüyorsa kart istemeyip durmayı seçer (Stand).
8- Eğer oyuncu 21`i geçerse oyunu kaybeder. (Bust) bu durumda krupiyerin elinin durumuna bakılmaksızın krupiyer oyunu kazanmış olur.
9- Bütün oyuncular kart almayı bitirdıkları zaman krupiyer kapalı kartını açar ve elindeki kartların toplam değeri 17`den az ise kart çekmeye devam eder, 17 ve daha büyük ise kart çekmeyi bırakır.
10- Krupiyer 21`i geçerse (bust) 21`i geçmeyen bütün oyuncular kazanmış olur.
11- Oyuncu ve krupiyer aynı skoru elde ederse (Push) oyunda herhangi bir kazanan olmaz.

class Card

    def  -- Kartları Tanımla
            Face ve Suit objelerini dön....
            "As" = [1, 11]
            Repr ve Str fonksiyonlarını olurştur.. f stringle

class CardDecking (Adem)

    

    def -- kart ver ()
            1 - Random olarak gerekli oyuncuya kart ver.
    def -- player kart göster
            2 - Player'ın iki kartınıda ve yanıda toplamını göster. (Sum of CardValues)
    def -- dealer kart göster ve sakla
            3 - Dealer'ın bir kartını göster diğerini ******* gizle. tek kartın değeerini yaz.
    def -- kart çıkar ()
            4 - ilk elde verilen kartları ve çekilen kartları kart havuzundan çıkar.
    def -- Status (Böyle bir fonksiyona gerek yok çünkü bunu game class'ı içerisinde blackjack kontrol kısmında tekrardan yapmış bulıunuyoruz.)
            5 - İlk aşamada BlackJack durumunu kontrol et, varsa bitir.
                BlackJack durumu ikisinde de varsa, beraberlik.

Class Game
    def -- BlackJack_Kontrol (Emre)
           Player ve Dealer' a ikişer kart ver... (CardDecking.kart ver)
           BlackJack kontrol et. CardValues den çek.. if statemen koy.

    def -- Sum of CardValues(player, dealer) (Emre)

    def -- status Taner
        6 - Döngü: Oyuncu stand demezse, kart ver. (CardDecking(kart_ver))
                   Oyuncu 21'e ulaşırsa döngüden çık makineye kart ver.
                   Oyuncu 21 i geçerse oyunu bitir.
    def -- stand   Taner
        7 - Stand Derse : Makinenin görünmeyen kartını aç. return True False
    def -- DealerTurn Alperen
        Makine 17ye eşit yada geçene kadar kart ver.
    def -- Finish_Set: Alperen
        8 - BlackJack_Kontrol True ise bitir.
        8 - Makine 17'ye ulaştığında yada 21'i geçtiğinde oyunu bitir.
        9 - Toplam değerleri kıyasla büyük olanı galip ata.

    def -- Finish_Game Emre
        10 - Oyunu bitirmek isterse bitir... ve kazanma toplamlarını bas.



"""

"""Card class that represents a playing card and its image file name."""

import secrets

FACES = ['Ace', '2', '3', '4', '5', '6','7', '8', '9', '10', 'Jack', 'Queen', 'King']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']


Ace = [1, 11]

Values = {'Ace': [1, 11], 'Jack': 10, 'Queen': 10, 'King': 10}

class CardDecking():

    def __init__(self):
        
    def card_giving(self): #gives cards
        players_faces=[]
        dealers_faces=[]
        players_suits=[]
        dealers_suits=[]
        
        total_player=o
        total_dealer=o
        for i in range(2):
            player_card_faces=secrets.choice(FACES) #random value from the list FACES
            player_card_suits=secrets.choice(SUITS)

            dealer_card_faces=secrets.choice(FACES)
            dealer_card_suits=secrets.choice(SUITS)
            
            if player_card_faces>=2 and player_card_faces<=10:
                total_player+=player_card_faces
            else:
                total_player+=Values.get(player_card_faces)
                
            if dealer_card_faces>=2 and dealer_card_faces<=10:
                total_dealer+=dealer_card_faces
            else:
                total_dealer+=Values.get(dealer_card_faces)
                
            
            players_faces.append(player_card_faces)
            players_suits.append(player_card_suits)
            dealers_faces.append(dealer_card_faces)
            dealers_suits.append(dealer_card_suits)
            
        print(f'players cards are {players_faces}, total value of  dealers card is {dealers_faces[0]}')
        a=[total_player, total_dealer,player_faces, dealer_faces]
        return a

    def show_players_cards(self):
        
        sum_of_card_values=card_giving()
        sum_of_player_values=sum_of_card_values[0]
        player_cards=sum_of_card_values[2]
        print(f'the total value of player is {sum_of_player_values}, the values are {player_cards}')

    def dealer_cards(self):
        sum_of_card_values=card_giving()
        one_of_dealer_value=sum_of_card_values[1]
        print(f'one value of dealer is {one_of_dealer_value}')
    
    def decreased_cards(self):
    
    def BlackJackControl(self):
        control=card_giving()
        if control[0]==21 and control[1]==21:
            print('the total amount of numbers are equal')
            break
        else:git
            continue


class Card:
    # constant variable'lar her zaman büyük yazılır.
    FACES = ['Ace', '2', '3', '4', '5', '6',
             '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    Ace = [1, 11]

    Values = {'Ace': [1, 11], 'Jack': 10, 'Queen': 10, 'King': 10}

    def __init__(self, face, suit):
        """Initialize a Card with a face and suit."""
        self._face = face
        self._suit = suit

    @property
    def face(self):
        """Return the Card's self._face value."""
        return self._face

    @property
    def suit(self):
        """Return the Card's self._suit value."""
        return self._suit

    def __repr__(self):
        # _repr object direk çağrıldığında çağrıldığında çağrılır.
        # bu her class siçerisinde muhakkak bulunur.
        # _str olmadığında bu otomatik olarak çağrılır.
        """Return string representation for repr()."""
        return f"Card(face='{self.face}', suit='{self.suit}')"

    def __str__(self):
        # _str object print içerisinde çağrıldığında çağrılır.
        """Return string representation for str()."""
        return f'{self.face} of {self.suit}'

    def __format__(self, format):
        """Return formatted string representation."""
        # Format fstring olarak çağrılınca format belirlemek için
        return f'{str(self):{format}}'


"""Deck class represents a deck of Cards."""


class DeckOfCards:

    def __init__(self):
        """Initialize the deck."""
        self._current_card = 0
        self._deck = []

    def card_distribute(self):
        while True:
            random_face = random.choice(Card.FACES)
            random_suit = random.choice(Card.SUITS)
            if [random_face, random_suit] not in self._deck:
                self._deck = self._deck.append([random_face, random_suit])
                break
            else:
                continue
        return self._deck[-1]

    def deal_card(self):
        """Return one Card."""
        try:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except:
            return None

    def __str__(self):
        """Return a string representation of the current _deck."""
        s = ''

        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}'
            if (index + 1) % 4 == 0:
                s += '\n'

        return s


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

    def sum_of_cards_values(self):
        for name, suit in self._cards_of_player:
            if type(name) != int:
                if name != 'Ace':
                    name = Card.Values[name]
                elif name == 'Ace':
                    if self._point_of_player <= 10:
                        name = Card.Values[name[1]]
                    else:
                        name = Card.Values[name[0]]
                self._point_of_player += name
            else:
                self._point_of_player += name

        for name, suit in self._cards_of_dealer:
            if type(name) != int:
                if name != 'Ace':
                    name = Card.Values[name]
                elif name == 'Ace':
                    if self._point_of_dealer <= 10:
                        name = Card.Values[name[1]]
                    else:
                        name = Card.Values[name[0]]
                self._point_of_dealer += name
            else:
                self._point_of_dealer += name

        self._points = [self._point_of_player, self._point_of_dealer]
        return self._points

    def black_jack_control(self):
        i = 0
        while i < 2:
            self._cards_of_player = self._cards_of_player.append(DeckOfCards.card_distribute())
            self._cards_of_dealer = self._cards_of_dealer.append(DeckOfCards.card_distribute())
            i += 1

        if Game.sum_of_cards_values()[0] == 21:
            return True
        else:
            return False

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

# ######################## Taner

    def __repr__(self):
        """Return string representation for repr()."""
        return f"Points(Player='{self._point_of_player}', Dealer='{self._point_of_dealer}')"

    def __str__(self):
        """Return string representation for str()."""
        return f'{self._point_of_player} of {self._point_of_dealer}'

    def finish_game(self):
        print("Thank you for playing with us")
        print(f' number of wins of player: %s' % self._total_wins_player,
              f'\n number of wins of dealer: %s' % self._total_wins_dealer,
              f'\n number of ties are: %s' % self._total_ties)
        if self._total_wins_player > self._total_wins_dealer:
            print("Player defeated the dealer")
        else:
            print("Dealer defeated the player")

    def print_results(self):
        print(f'Point of Player is: %s ' % self._point_of_player)
        print(f'Point of Dealer is: %s' % self._point_of_dealer)

    def finish_set(self):
        Game.print_results()
        if Game.black_jack_control():
            if Game.sum_of_cards_values()[1] < 21:
                print("*************************************")
                print("Congratulations! You got a Blackjack!\n")
                print("*************************************")
                self._total_wins_player += 1
            else:
                print("NO WINNER! TIE")
                self._total_ties += 1
        elif self._point_of_player == 21:
            if self._point_of_player > self._point_of_dealer:
                print("Congratulations. Your score is higher than the dealer. You win\n")
                self._total_wins_player += 1
            else:
                print("NO WINNER! TIE")
                self._total_ties += 1
        elif self._point_of_dealer == 21:
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



