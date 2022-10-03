from buyer import Buyer
from card import Card


class Marketplace:

    @classmethod
    def create_marketplace(cls):
        return cls(id_counter=0,
                   buyer_dict={},
                   record_counter=0,
                   card_dict={},
                   profit=0,
                   current_id=0,
                   market_record={})

    __id_counter: int
    __record_counter: int
    __buyer_dict: dict[int, Buyer]
    __card_dict: dict[str, Card]
    __market_record: dict[int: dict[str: str | Card]]
    __market_profit: int
    __current_id: int

    def __init__(
            self, id_counter: int,
            record_counter: int,
            buyer_dict: dict,
            card_dict: dict,
            profit: int,
            current_id: int,
            market_record: dict

    ) -> None:
        self.__id_counter = id_counter
        self.__record_counter = record_counter
        self.__buyer_dict = buyer_dict
        self.__card_dict = card_dict
        self.__market_profit = profit
        self.__current_id = current_id
        self.__market_record = market_record

    # Marketplace setters:

    def create_new_buyer(self, buyer_name: str) -> None:
        self.__id_counter += 1
        self.__buyer_dict[self.__id_counter] = Buyer.create_buyer(buyer_name)

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

    def select_id(self, input_id: int) -> None:
        self.__current_id = input_id

    def purchase(self, card_name: str, buyer_id: int) -> None:
        amount = self.__card_dict.get(card_name).get_price()
        self.__card_dict.get(card_name).remove_from_sale()
        self.__market_profit += amount
        self.__buyer_dict.get(buyer_id).purchase(amount, card_name, self.__card_dict[card_name])
        self.__record_counter += 1
        self.__market_record[self.__record_counter] = {
            "buyer_id": buyer_id,
            "card_name": card_name,
            "price": amount,
            "card": self.__card_dict.get(card_name)
        }
        self.remove_card_from_sale(card_name)

    def add_buyer_coins(self, buyer_id: int, amount: int) -> None:
        self.__buyer_dict.get(buyer_id).add_coins(amount)

    def can_purchase(self, card_name: str, buyer_id: int) -> bool:
        return (
                self.__card_dict[card_name].is_for_sale() and self.__buyer_dict[buyer_id].get_balance() >=
                self.__card_dict[card_name].get_price()
        )

    def get_current_id(self) -> int:
        return self.__current_id

    # Record cards getters:

    def has_cards_in_record(self) -> bool:
        return self.__record_counter > 0

    def has_this_card_in_record(self, purchase_id: int) -> bool:
        return purchase_id in self.__market_record.keys()

    def get_record_cards(self) -> str:
        record_cards = ""
        for record in self.__market_record.values():
            record_cards += (
                f"\n██║ Purchase ID: {self.get_record_purchase_id(record.get('card_name'))}" +
                f"\n██║ Buyer ID: {record.get('buyer_id')}" +
                f"\n██║ Name: {record.get('card_name')}" +
                f"\n██║ Price: {record.get('price')}\n"
            )
        return record_cards

    def get_record_purchase_id(self, card_name: str) -> int:
        for key, value in self.__market_record.items():
            if value["card_name"] == card_name:
                return key

    def get_card_from_record(self, purchase_id: int) -> str:
        return self.__market_record[purchase_id]["card"]

    # Listed cards getters:

    def get_listed_cards(self) -> str:
        listed_cards = ""
        for card in self.__card_dict.keys():
            listed_cards += (
                f"\n██║ Name: {card}" +
                f"\n██║ Price: {self.get_card_price(card)}" +
                f"\n██║ For sale: {self.card_is_for_sale(card)}\n"
            )
        return listed_cards

    def has_cards_for_sale(self) -> bool:
        return len(self.__card_dict) > 0

    def has_card(self, card_name: str) -> bool:
        return card_name in self.__card_dict.keys()

    def get_card_stats(self, card_name: str) -> Card:
        return self.__card_dict[card_name]

    def get_card_price(self, card_name: str) -> int:
        return self.__card_dict.get(card_name).get_price()

    def card_is_for_sale(self, card_name: str) -> bool:
        return self.__card_dict[card_name].is_for_sale()

    # Buyer getters:

    def has_buyers(self) -> bool:
        return len(self.__buyer_dict) > 0

    def buyer_exists(self, buyer_id: int):
        return buyer_id in self.__buyer_dict.keys()

    def get_buyer_list(self) -> str:
        buyer_list = "\n██╗ Registered buyers:\n"
        for buyer in self.__buyer_dict.keys():
            buyer_list += f"██║ {self.__buyer_dict.get(buyer)}\n"
        return buyer_list

    def get_buyer(self, buyer_id: int) -> Buyer:
        return self.__buyer_dict.get(buyer_id)

    def get_buyer_id(self, name: str) -> int:
        for key, value in self.__buyer_dict.items():
            if value.get_buyer_name() == name:
                return key

    def buyer_has_cards(self, user_id: int) -> bool:
        return self.__buyer_dict[user_id].has_cards()

    def buyer_owns_this_card(self, user_id: int, name: str) -> bool:
        return self.__buyer_dict[user_id].owns_this_card(name)

    def get_buyer_cards(self, user_id: int) -> str:
        return self.__buyer_dict[user_id].owned_cards()

    def get_buyer_card_stats(self, user_id: int, name: str) -> str:
        return self.__buyer_dict[user_id].owned_card_stats(name)

    def get_buyer_name(self, user_id: int) -> str:
        return self.__buyer_dict.get(user_id).get_buyer_name()

    def get_buyer_balance(self, buyer_id: int) -> int:
        return self.__buyer_dict.get(buyer_id).get_balance()

    def get_buyer_spent_coins(self, buyer_id: int) -> int:
        return self.__buyer_dict.get(buyer_id).get_coins_spent()

    # Listed and Record cards deleters:

    def remove_card_from_sale(self, card_name: str) -> None:
        del self.__card_dict[card_name]

    def remove_card_from_record(self, purchase_id: int) -> None:
        del self.__market_record[purchase_id]

    # Marketplace representation method:

    def __str__(self) -> str:
        return (
            f"""
██╗ Market profit: {self.__market_profit}
██║ Number of sold cards: {self.__record_counter}
██║ Number of cards listed: {len(self.__card_dict.keys())}
██║ Number of buyers: {self.__id_counter}
╚═╝
"""
        )
