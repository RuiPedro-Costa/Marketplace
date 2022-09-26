class Card:

    @classmethod
    def create_card(cls, name: str, overall: int, position: str, team: str, price: int):
        return cls(name, overall, position, team, price, state=True)

    __name: str
    __overall: int
    __position: str
    __team: str
    __price: int
    __for_sale: bool

    POSITIONS: dict[str, str] = {
        'DL': 'Defesa Lateral',
        'DC': 'Defesa Central',
        'MC': 'Médio Centro',
        'ML': 'Médio Lareal',
        'AC': 'Avançado Centro',
        'EX': 'Extremo',
        'GR': 'Guarda Redes',
    }

    def __init__(self, name: str, overall: int, position: str, team: str, price: int, state: bool) -> None:
        self.__name = name
        self.__overall = overall
        self.__position = position
        self.__team = team
        self.__price = price
        self.__for_sale = state

    def remove_from_sale(self) -> None:
        self.__for_sale = False

    def get_price(self) -> int:
        return self.__price

    def get_overall(self) -> int:
        return self.__overall

    def is_for_sale(self) -> bool:
        return self.__for_sale

    def __str__(self) -> str:
        return (f"""
████████████████████████████████╗
██╔═════════════════════════════╝
██║ Name: {str(self.__name)}
██║ Overall: {str(self.__overall)}
██║ Position: {str(self.POSITIONS.get(self.__position))}
██║ Team: {str(self.__team)}
██║ Price: {str(self.__price)}
██║ For Sale: {str(self.__for_sale)}
██║
████████████████████████████████╗
╚═══════════════════════════════╝
"""
                )
