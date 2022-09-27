class Buyer:
    @classmethod
    def create_buyer(cls, buyer_name: str):
        return cls(buyer_name=buyer_name, coins=0, coins_spent=0)

    __buyer_name: str
    __coins: int
    __coins_spent: int

    def __init__(self, buyer_name: str, coins: int, coins_spent: int) -> None:
        self.__buyer_name = buyer_name
        self.__coins = coins
        self.__coins_spent = coins_spent

    def add_coins(self, amount: float) -> None:
        self.__coins += amount

    def purchase(self, price: float) -> None:
        self.__coins -= price
        self.__coins_spent += price

    def get_balance(self) -> int:
        return self.__coins

    def get_coins_spent(self) -> int:
        return self.__coins_spent

    def __str__(self):
        return f"Name: {self.__buyer_name}, Coins Spent: {self.__coins_spent}."
