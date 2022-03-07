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
        to_print = {}
        if self._hair:
            to_print['Hair'] = self._italic_value(self._hair)

        if self._collar:
            to_print['Collar'] = self._italic_value(self._collar)

        if self._upper_half:
            to_print['Upper Half'] = self._italic_value(self._upper_half)

        if self._bracelet:
            to_print['Bracelet'] = self._italic_value(self._bracelet)

        if self._lower_half:
            to_print['Lower Half'] = self._italic_value(self._lower_half)

        if self._shoes:
            to_print['Shoes'] = self._italic_value(self._shoes)

        value = self.get_printable_output(to_print)

        return value

    @staticmethod
    def _italic_value(s: ClothingPart):
        return f'\x1B[3m{s}\x1B[0m'

    @staticmethod
    def get_printable_output(p: dict):
        to_print = ''

        keys = list(p.keys())
        items = list(p.values())
        biggest_key = ''
        biggest_item = ''

        for i in range(len(p)):
            if len(keys[i]) > len(biggest_key):
                biggest_key = keys[i]
            if len(items[i]) > len(biggest_item):
                biggest_item = items[i]

        biggest_key = len(biggest_key)
        biggest_item = len(biggest_item)

        for i in range(len(p)):
            t: str = keys[i]
            t = t.ljust(biggest_key)

            to_print += t
            to_print += '  ---  '

            t: str = items[i]
            t = t.ljust(biggest_item)
            to_print += t + '\n'

        return to_print
