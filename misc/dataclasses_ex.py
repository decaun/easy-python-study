# https://realpython.com/python-data-classes/

from dataclasses import dataclass
from typing import Any

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42



from math import asin, cos, radians, sin, sqrt

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin(sqrt(h))


from dataclasses import dataclass, field
from typing import List

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'



if __name__=="__main__":
    pos = Position('Oslo', 10.8, 59.9)
    print(pos)
    print(pos.lat)
    print(Position('Null Island'))
    oslo = Position('Oslo', 10.8, 59.9)
    vancouver = Position('Vancouver', -123.1, 49.3)
    print("oslo.distance_to(vancouver)")
    print(oslo.distance_to(vancouver))
    print(Deck())