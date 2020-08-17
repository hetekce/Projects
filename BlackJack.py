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


1 - Player ve Dealer'a ikişer kart ver.
2 - Player'ın iki kartınıda ve yanıda toplamını göster.
3 - Dealer'ın bir kartını göster diğerini ******* gizle. tek kartın değeerini yaz.
4 - ilk elde verilen kartları ve çekilen kartları kart havuzundan çıkar.

5 - İlk aşamada BlackJack durumunu kontrol et, varsa bitir.
    BlackJack durumu ikisinde de varsa, beraberlik.
6 - Döngü: Oyuncu stand demezse, kart ver.
           Oyuncu 21'e ulaşırsa döngüden çık makineye kart ver.
           Oyuncu 21 i geçerse oyunu bitir.
7 - Stand Derse : Makinenin görünmeyen kartını aç...
    Makine 17ye eşit yada geçene kadar kart ver.
8 - Makine 17'ye ulaştığında yada 21'i geçtiğinde oyunu bitir.
9 - Toplam değerleri kıyasla büyük olanı galip ata.
10 - Oyunu bitirmek isterse bitir... ve kazanma toplamlarını bas.



"""


"""Card class that represents a playing card and its image file name."""


class Card:
    # constant variable'lar her zaman büyük yazılır.
    FACES = ['Ace', '2', '3', '4', '5', '6',
             '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

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

    @property
    def image_name(self):
        """Return the Card's image file name."""
        # str type casting replace method unu kullanmak için
        # normalde self object'in kendisidir
        return str(self).replace(' ', '_') + '.png'

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
    NUMBER_OF_CARDS = 52  # constant number of Cards

    def __init__(self):
        """Initialize the deck."""
        self._current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % 13],
                                   Card.SUITS[count // 13]))

    def shuffle(self):
        """Shuffle deck."""
        self._current_card = 0
        random.shuffle(self._deck)

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
