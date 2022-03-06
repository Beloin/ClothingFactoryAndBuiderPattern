class ClothingPart:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name


class Clothing:
    _lower_half = None
    _upper_half = None
    _shoes = None
    _collar = None
    _hair = None
    _bracelet = None

    def set_lower_half(self, lower_half: ClothingPart):
        self._lower_half = lower_half

    def set_upper_half(self, upper_half: ClothingPart):
        self._upper_half = upper_half

    def set_shoes(self, shoes: ClothingPart):
        self._shoes = shoes

    def set_collar(self, collar: ClothingPart):
        self._collar = collar

    def set_hair(self, hair: ClothingPart):
        self._hair = hair

    def set_bracelet(self, bracelet: ClothingPart):
        self._bracelet = bracelet

    def __repr__(self) -> str:
        value = ''

        if self._hair:
            value += f'Hair --- {self._italic_value(self._hair)}\n'

        if self._collar:
            value += f'Collar --- {self._italic_value(self._collar)}\n'

        if self._upper_half:
            value += f'Upper Half --- {self._italic_value(self._upper_half)}\n'

        if self._bracelet:
            value += f'Bracelet --- {self._italic_value(self._bracelet)}\n'

        if self._lower_half:
            value += f'Lower Half --- {self._italic_value(self._lower_half)}\n'

        if self._shoes:
            value += f'Shoes --- {self._italic_value(self._shoes)}\n'

        return value

    @staticmethod
    def _italic_value(s: ClothingPart):
        return f'\x1B[3m{s}\x1B[0m'
