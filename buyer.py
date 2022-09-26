class Buyer:
    @classmethod
    def create_buyer(cls, buyer_name: str, buyer_id: int):
        return cls(buyer_name=buyer_name, buyer_id=buyer_id, coins=0, coins_spent=0)

    __buyer_name: str
    __buyer_id: int
    __coins: int
    __coins_spent: int

    def __init__(self, buyer_name: str, buyer_id: int, coins: int, coins_spent: int) -> None:
        self.__buyer_name = buyer_name
        self.__buyer_id = buyer_id
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
