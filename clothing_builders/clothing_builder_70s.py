from clothing import ClothingPart, Clothing
from clothing_builders.clother_builder import ClothingBuilder


class ClothingBuilder70s(ClothingBuilder):
    _clothing = Clothing()

    def get_clothing(self) -> Clothing:
        return self._clothing

    def build_lower_half(self) -> 'ClothingBuilder':
        self._clothing.set_lower_half(ClothingPart('Bell Bottom Blue Pants'))
        return self

    def build_upper_half(self) -> 'ClothingBuilder':
        self._clothing.set_upper_half(ClothingPart('White X-Pattern Cropped'))
        return self

    def build_shoes(self) -> 'ClothingBuilder':
        self._clothing.set_shoes(ClothingPart('Blue Start Pattern High Wheels'))
        return self

    def build_collar(self) -> 'ClothingBuilder':
        self._clothing.set_collar(None)
        return self

    def build_hair(self) -> 'ClothingBuilder':
        self._clothing.set_hair(ClothingPart('Curly Hair'))
        return self

    def build_bracelet(self) -> 'ClothingBuilder':
        self._clothing.set_bracelet(None)
        return self

