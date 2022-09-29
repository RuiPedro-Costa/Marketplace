from card import Card


class Buyer:
    @classmethod
    def create_buyer(cls, buyer_name: str):
        return cls(buyer_name=buyer_name, coins=0, coins_spent=0, card_collection={})

    __buyer_name: str
    __coins: int
    __coins_spent: int
    __card_collection: dict[str: Card]

    def __init__(self, buyer_name: str, coins: int, coins_spent: int, card_collection: dict) -> None:
        self.__buyer_name = buyer_name
        self.__coins = coins
        self.__coins_spent = coins_spent
        self.__card_collection = card_collection

    def add_coins(self, amount: float) -> None:
        self.__coins += amount

    def purchase(self, price: float,card_name: str, card: Card) -> None:
        self.__coins -= price
        self.__coins_spent += price
        self.__card_collection[card_name] = card

    def get_balance(self) -> int:
        return self.__coins

    def get_coins_spent(self) -> int:
        return self.__coins_spent

    def get_buyer_name(self) -> str:
        return self.__buyer_name

    def owns_this_card(self, card_name: str) -> bool:
        return card_name in self.__card_collection.keys()

    def has_cards(self) -> bool:
        if len(self.__card_collection) > 0:
            return True
        return False

    def owned_cards(self) -> str:
        card_collection = ""
        for card in self.__card_collection.keys():
            card_collection += (
                f"\n██║ Name: {card}"
            )
        return card_collection

    def owned_card_stats(self, name: str) -> str:
        return self.__card_collection.get(name)

    def __str__(self):
        return (
            f"""
██╗ Buyer:
██║ Name: {self.__buyer_name}
██║ Coins Spent: {self.__coins_spent}
██║ Number of Cards: {len(self.__card_collection)}
╚═╝\n
"""
        )
