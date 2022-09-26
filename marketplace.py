from typing import Optional
from buyer import Buyer
from card import Card


class Marketplace:

    # buyer id nao esta correto.

    @classmethod
    def create_marketplace(cls, buyer_name, buyer_id):
        return cls(buyer=Buyer.create_buyer(buyer_name, buyer_id), card=None)

    __buyer_id_counter: int
    __buyer: Buyer
    __card: Optional[Card]

    def __init__(self, buyer_id_counter: int, buyer: Buyer, card: Card | None) -> None:
        self.__buyer_id_counter = buyer_id_counter
        self.__buyer = buyer
        self.__card = card

    def list_card(self, name: str, overall: int, position: str, club: str, price: int) -> None:
        can_be_sold = False
        if (40 <= overall < 50) and price >= 250:
            can_be_sold = True
        elif (50 <= overall < 65) and price >= 400:
            can_be_sold = True
        elif (65 <= overall < 75) and price >= 550:
            can_be_sold = True
        elif (75 <= overall < 83) and price >= 750:
            can_be_sold = True
        elif (83 <= overall < 85) and price >= 1000:
            can_be_sold = True
        elif (85 <= overall < 87) and price >= 2000:
            can_be_sold = True
        elif (87 <= overall < 90) and price >= 5000:
            can_be_sold = True
        elif overall == 90 and price >= 10000:
            can_be_sold = True
        elif overall == 91 and price >= 15000:
            can_be_sold = True
        elif overall == 92 and price >= 20000:
            can_be_sold = True
        if can_be_sold and position in Card.POSITIONS.keys():
            self.__card = Card.create_card(name, overall, position, club, price)

    def purchase(self) -> None:



    def reject_card(self) -> None:



    def remove_card(self) -> None:
        self.__card = None

    def add_buyer_coins(self, amount: int) -> None:
        self.__buyer.add_coins(amount)

    def get_market_profit(self) -> float:
        return self.__buyer.get_coins_spent()

    def get_card_stats(self) -> Card:
        return self.__card

    def get_card_price(self) -> int:
        return self.__card.get_price()

    def has_card(self) -> bool:
        return self.__card is not None

    def has_card_for_sale(self) -> bool:
        return self.__card.is_for_sale()

    def can_purchase(self) -> bool:
        return self.__card.is_for_sale() and self.__buyer.get_balance() >= self.__card.get_price()

    def get_buyer(self) -> Buyer:
        return self.__buyer.__str__()

    def get_buyer_balance(self) -> int:
        return self.__buyer.get_balance()

    def get_buyer_spent_coins(self) -> int:
        return self.__buyer.get_coins_spent()
