from buyer import Buyer
from card import Card

# dicionarios nao funcionam

class Marketplace:

    @classmethod
    def create_marketplace(cls):
        return cls(id_counter=0, card_counter=0, buyer_dict={}, card_dict={})

    __id_counter: int
    __card_counter: int
    __market_profit: int
    __buyer_dict: dict
    __card_dict: dict

    def __init__(self, id_counter: int, card_counter: int, buyer_dict: dict, card_dict: dict) -> None:
        self.__id_counter = id_counter
        self.__card_counter = card_counter
        self.__buyer_dict = buyer_dict
        self.__card_dict = card_dict

    def create_new_buyer(self, buyer_name: str) -> None:
        self.__buyer_dict[self.__id_counter + 1] = Buyer.create_buyer(buyer_name, self.__id_counter + 1)

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
            self.__card_dict[name] = Card.create_card(name, overall, position, club, price)

    def purchase(self, card_name: str, buyer_id: int) -> None:
        amount = self.__card_dict[card_name].get_price()
        self.__card_dict[card_name].remove_from_sale()
        self.__market_profit += amount
        self.__buyer_dict[buyer_id].purchase(amount)

    # def reject_card(self, card_name: str) -> None:
    #     self.__card_dict[card_name].remove_from_sale()

    def remove_card(self, card_name: str) -> None:
        del self.__card_dict[card_name]

    def add_buyer_coins(self, buyer_id: int, amount: int) -> None:
        self.__buyer_dict[buyer_id].add_coins(amount)

    def get_market_profit(self) -> int:
        return self.__market_profit

    def get_card_stats(self, card_name: str) -> Card:
        return self.__card_dict.get(card_name)

    def get_card_price(self, card_name: str) -> int:
        return self.__card_dict[card_name].get_price()

    def has_card(self) -> bool:
        return self.__card_dict is not None

    def has_card_for_sale(self, card_name: str) -> bool:
        return self.__card_dict[card_name].is_for_sale()

    def can_purchase(self, card_name: str, buyer_id: int) -> bool:
        return self.__card_dict[card_name].is_for_sale() and self.__buyer_dict[buyer_id].get_balance() >= self.__card_dict[card_name].get_price()

    def get_buyer(self, buyer_id: int) -> Buyer:
        return self.__buyer_dict[buyer_id]

    def get_buyer_balance(self, buyer_id: int) -> int:
        return self.__buyer_dict[buyer_id].get_balance()

    def get_buyer_spent_coins(self, buyer_id: int) -> int:
        return self.__buyer_dict[buyer_id].get_coins_spent()


m = Marketplace.create_marketplace()
c1 = m.list_card("ze", 80, "gr", "xepa", 800)
c2 = m.list_card("asdasd", 90, "gr", "xepa", 10000)

print(m.get_card_stats("ze"))
